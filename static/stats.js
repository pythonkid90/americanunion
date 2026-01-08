// function newRow(cellToEdit, locationClicked) {
//     const newRow = document.createElement("tr");

//     if (locationClicked == "bottom") { cellToEdit.after(newRow) } else { cellToEdit.before(newRow) }

//     const table_id = cellToEdit.parentNode.parentNode.parentNode.id

//     const unions_columns = ["Name", "Leader", "Reserve", "Reps.", "Military", "Land", "Members", "Other"];
//     const nations_columns = ["Name", "Leader", "Wealth", "Citizens", "Military", "Location/Land", "Other"];
//     const columns = (table_id === "unions") ? unions_columns : nations_columns;

//     let index = 0;

//     for (const column of columns) {
//         newCell = document.createElement("td");
//         newCell.setAttribute("class", `newCell ${column}`);
//         newRow.appendChild(newCell);

//         if (column === "Name") {
//             newCell.innerHTML = "Nation Name Here"
//             newCell.focus()
//         } else {
//             newCell.innerHTML = 0;
//         }
//         index += 1;
//     }
// }

let cellsEdited = new Map();

for (const element of document.querySelectorAll("table")) {
    element.addEventListener("click", function(event) {
        let cellToEdit = event.target;

        cellToEdit.setAttribute("contenteditable", "true");
        cellToEdit.setAttribute("spellcheck", "false");
        cellToEdit.focus();
    });

    element.addEventListener("mouseenter", function(event) {
        let cellToEdit = event.target;
        const rect = cellToEdit.getBoundingClientRect();

        if (rect.bottom - event.clientY <= 15) {
            newRow(cellToEdit, "bottom")
        } else if (event.clientY - rect.top <= 15) {
            newRow(cellToEdit, "top")
        }
    });

    element.addEventListener("blur", function(event) {
        let cellToEdit = event.target;
        cellToEdit.removeAttribute("contenteditable");
        cellToEdit.removeAttribute("spellcheck");

        if (cellToEdit.textContent.includes("newCell")) {
            const newName = cellToEdit.firstChild.textContent;
            cellToEdit.textContent = newName + cellToEdit.textContent.split(" ", 2)[1]
        }

        cellsEdited.set(cellToEdit.className, cellToEdit.innerHTML);
        navigator.sendBeacon("/stats/save", JSON.stringify(Object.fromEntries(cellsEdited)));
        
    }, true)
}