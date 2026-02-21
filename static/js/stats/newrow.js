import {addUpdatedCell, sendUpdatedCells, getCellInfo, unions_columns, nations_columns} from './globals.js';

export function createNewRow(cellToEdit, locationClicked) {
    const newRow = document.createElement("tr");

    if (locationClicked == "bottom") { 
        cellToEdit.parentNode.after(newRow); 
    } else { 
        cellToEdit.parentNode.before(newRow); 
    }

    const cellInfoList = getCellInfo(cellToEdit)
    const tableID = cellInfoList["Table"];

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

    const rowIdentifier = `${cellInfoList["ID"]} ${cellInfoList["Table"]}`
    let newRowInfo = {
        [rowIdentifier]: {}
    }
    for (const column of columns) {
        const newCell = document.createElement("td");

        newCell.innerHTML = columnDefaults[column];

        newRow.appendChild(newCell);
        newRowInfo[rowIdentifier][column] = columnDefaults[column];
    }

    navigator.sendBeacon("/stats/new", JSON.stringify(newRowInfo));
}

