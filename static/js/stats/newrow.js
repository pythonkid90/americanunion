import {addUpdatedCell, sendUpdatedCells} from './globals.js';

export function createNewRow(cellToEdit, locationClicked) {
    const newRow = document.createElement("tr");

    if (locationClicked == "bottom") { 
        cellToEdit.parentNode.after(newRow); 
    } else { 
        cellToEdit.parentNode.before(newRow); 
    }

    const tableID = cellToEdit.closest("section").id;
    const cellInfoList = cellToEdit.dataset.cellinfo.split(" ");

    const unions_columns = ["Name", "Leader", "Reserve", "Reps.", "Military", "Land", "Members", "Other"];
    const nations_columns = ["Name", "Leader", "Wealth", "Citizens", "Military", "Location/Land", "Other"];
    const columns = (tableID === "unions") ? unions_columns : nations_columns;
    
    const columnDefaults = {
        "Name": `${tableID[0].toUpperCase()}${tableID.slice(1, -1)} Name Here`,
        "Leader": "Leader Name(s) Here",
        "Reserve": "$0.0T",
        "Wealth": "$0.0T",
        "Reps.": "<span class='reps'>0</span><div class='rep-ratio'>(Citizen to Rep Ratio: 100000:1)</div>",
        "Citizens": "0M",
        "Land": `Describe the land ownings of this ${tableID.slice(0, -1)}.`,
        "Location/Land": `Describe the land ownings of this ${tableID.slice(0, -1)}.`,
        "Military": `Describe the military of this ${tableID.slice(0, -1)}. It may be subjective, and it should be qualitative.`,
        "Members": "Add Members! (Partial: Add Partial Members!)",
        "Other": `Give any other important information or titles to documents about this ${tableID.slice(0, -1)}.`
    };

    for (const column of columns) {
        const newCell = document.createElement("td");
        newCell.setAttribute("data-cellInfo", `newCellAfter${cellInfoList[0]} ${tableID} ${column}`);

        newCell.innerHTML = columnDefaults[column];

        newRow.appendChild(newCell);
        addUpdatedCell(newCell);
    }

    sendUpdatedCells();
}

