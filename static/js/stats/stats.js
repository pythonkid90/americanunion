import {addUpdatedCell, sendUpdatedCells, rowSelectInfo} from './globals.js';
import {activateDeleteOrPaintButtons, selectionUIMode, deleteOrPaintRows} from './actionbuttons.js';
import {createNewRow} from './newrow.js';

function updateRowIDs(row) {
    let rowCounter = -1;

    for (const tableRow of row.closest("table").querySelectorAll("tr")) {
        console.log(tableRow, row, rowCounter)
        for (const tableCell of tableRow.querySelectorAll("td")) {
            let cellInfoList = tableCell.dataset.cellinfo.split(" ")
            cellInfoList[0] = rowCounter
            tableCell.dataset.cellinfo = cellInfoList.join(" ");
        }

        rowCounter += 1
    }


}

function editCell(event) {
    if (event.target.tagName === "TD" || event.target.tagName === "DIV") {
        let cellToEdit = event.target;
        if (event.target.className === "rep-ratio") {
            cellToEdit = event.target.parentNode;
        }
            
        // Updates ID of cell to edit
        updateRowIDs(cellToEdit.parentNode)

        const cellInfoList = cellToEdit.dataset.cellinfo.split(" ");

        if (!rowSelectInfo["mode"]) {
            // Creates new row if near border.
            const rect = cellToEdit.getBoundingClientRect();

            if (rect.bottom - event.clientY <= 15) {
                createNewRow(cellToEdit, "bottom");
            } else if (event.clientY - rect.top <= 15) {
                createNewRow(cellToEdit, "top");
            } else {
                event.target.setAttribute("contenteditable", "true");
                event.target.setAttribute("spellcheck", "false");
                event.target.focus();
            }    
        } else {
            deleteOrPaintRows(cellToEdit.parentNode, cellInfoList);
        }
    }
}

// Trigger row selection when delete or paint buttons pressed.
document.querySelector(".action-buttons").addEventListener("click", activateDeleteOrPaintButtons)

// Trigger table changes
for (const table of document.querySelectorAll("table")) {
    table.addEventListener("click", editCell);

    table.addEventListener("blur", function(event) {

        let cellToEdit = event.target
        if (event.target.className === "rep-ratio") {
            cellToEdit = event.target.parentNode;
        }

        addUpdatedCell(cellToEdit);
        sendUpdatedCells();
    }, true);

    selectionUIMode(table)
}

