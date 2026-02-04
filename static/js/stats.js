// CELL/ROW MANIPULATION HELPER FUNCS
function createNewRow(cellToEdit, locationClicked) {
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
        "Reps.": "0",
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

function deleteOrPaintRows(rowClicked, cellInfoList) {
    document.querySelector("#action-instructions").style.display = "none";
    rowSelectMode = false;

    if (rowSelectType === "delete-row") {
        fetch(`/stats/delete/${cellInfoList[1]}/${cellInfoList[0]}`, {method: 'DELETE'})
        rowClicked.remove()
    } else if (rowClicked.closest("section").id === "nations") {
        document.querySelector("#repaint").style.display = "block";

        document.querySelector("#repaint-submit").addEventListener("click", function() {
            document.querySelector("#repaint").style.display = "none";

            const submittedHexValue = document.querySelector("#repaint-hex").value
            rowClicked.style.backgroundColor = `#${submittedHexValue}`
            navigator.sendBeacon("/stats/save", `{"${cellInfoList[0]} Nations Background": "#${submittedHexValue}"}`);

        }, {once: true})

        document.querySelector("#repaint-cancel").addEventListener("click", function() {
            document.querySelector("#repaint").style.display = "none";
        }, {once: true})
    } else {
        document.querySelector("#action-instructions").style.display = "block";
        rowSelectMode = true;
    }
}

function addUpdatedCell(cellToEdit) {
    cellToEdit.removeAttribute("contenteditable");
    cellToEdit.removeAttribute("spellcheck");

    cellsEdited.set(cellToEdit.dataset.cellinfo, cellToEdit.textContent);
}

function sendUpdatedCells() {
    navigator.sendBeacon("/stats/save", JSON.stringify(Object.fromEntries(cellsEdited)));
    cellsEdited.clear();
}
        
let cellsEdited = new Map();
let rowSelectMode = false;
let rowSelectType = "";

// TABLE EVENT LISTENERS
for (const table of document.querySelectorAll("table")) {
    table.addEventListener("click", function(event) {
        if (event.target.tagName === "TD" || event.target.tagName === "SPAN") {

            let cellToEdit = event.target;
            if (event.target.tagName === "SPAN") {
                cellToEdit = event.target.parentNode;
            }
                
            const cellInfoList = cellToEdit.dataset.cellinfo.split(" ");

            // Fixes ID of newCells so that the Python recognizes the ID.
            if (cellInfoList[0].startsWith("newCell")) {
                cellInfoList[0] = Number(cellInfoList[0].split("After")[1]) + 1;
                cellToEdit.dataset.cellinfo = cellInfoList.join(" ");
            }

            if (!rowSelectMode) {
                // Creates new row if near border.
                const rect = cellToEdit.getBoundingClientRect();

                if (rect.bottom - event.clientY <= 15) {
                    createNewRow(cellToEdit, "bottom");
                } else if (event.clientY - rect.top <= 15) {
                    createNewRow(cellToEdit, "top");
                } else {
                    cellToEdit.setAttribute("contenteditable", "true");
                    cellToEdit.setAttribute("spellcheck", "false");
                    cellToEdit.focus();
                }    
            } else {
                deleteOrPaintRows(event.target.parentNode, cellInfoList);
            }
        }
    });

    table.addEventListener("blur", function(event) {
        addUpdatedCell(event.target);
        sendUpdatedCells();
    }, true);

    table.addEventListener("mouseenter", function(event) {
        if (rowSelectMode && event.target.tagName === "TD") {
            if (rowSelectType === "delete-row" || event.target.closest("section").id === "nations") {
                event.target.parentNode.classList.add("row-selection-mode");
            }
        }
    }, true);

    table.addEventListener("mouseleave", function(event) {
        if (rowSelectMode && event.target.tagName === "TD") {
            event.target.parentNode.classList.remove("row-selection-mode");
        }
    }, true);
}

// Trigger row selection when delete or paint buttons pressed
document.querySelector(".action-buttons").addEventListener("click", function(event) {
    let popup = document.querySelector("#action-instructions")
    const buttonPressed = event.target.closest(".button-pill")

    if (popup.style.display !== "block" || rowSelectType !== buttonPressed.id) {
        popup.style.display = "block";
        rowSelectMode = true;
        rowSelectType = buttonPressed.id

        if (buttonPressed.id === "delete-row") {
            document.querySelector("#repaint").style.display = "none";
            popup.textContent = "Click on a row to delete it."
            
        } else if (buttonPressed.id === "paint-row") {
            popup.textContent = "Click on a row to change its background color."
        }
    } else {
        popup.style.display = "none";
        rowSelectMode = false;
    }
})