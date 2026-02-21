import {addUpdatedCell, sendUpdatedCells, rowSelectInfo, getCellInfo} from './globals.js';
import {activateDeleteOrPaintButtons, selectionUIMode, deleteOrPaintRows} from './actionbuttons.js';
import {createNewRow} from './newrow.js';

function editCell(event) {
    if (event.target.tagName === "TD" || event.target.tagName === "DIV") {
        let cellToEdit = event.target;
        if (event.target.className === "rep-ratio") {
            cellToEdit = event.target.parentNode;
        }
            
        // Updates ID of cell to edit
        const cellInfoList = getCellInfo(cellToEdit);

        if (!rowSelectInfo["mode"]) {
            // Creates new row if near border.
            const rect = cellToEdit.getBoundingClientRect();

            if (rect.bottom - event.clientY <= 10) {
                createNewRow(cellToEdit, "bottom");
            } else if (event.clientY - rect.top <= 10) {
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

document.querySelector("#map-upload").addEventListener('change', function (event) {
    const colonyMap = event.target.files[0];
    if (colonyMap && colonyMap.type === "image/png") {
        const colonyMapData = new FormData();
        colonyMapData.append('new-colony-map', colonyMap);

        fetch('/stats/map_upload', {
            method: 'PUT',
            body: colonyMapData
        })
        .catch((error) => {
            console.error('Error:', error);
        });

        // Update image to a blob URL so that it will show the new image without reload.
        document.querySelector("#colony-map").src = URL.createObjectURL(colonyMap);
        document.querySelector("#map-download").href = URL.createObjectURL(colonyMap);
    }
});