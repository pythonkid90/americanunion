let cellsEdited = new Map();
export let rowSelectInfo = {"mode": false, "type": ""}
export const unions_columns = ["Name", "Leader", "Reserve", "Reps.", "Military", "Land", "Members", "Other"];
export const nations_columns = ["Name", "Leader", "Wealth", "Citizens", "Military", "Location/Land", "Other"];

export function getCellInfo(cell) {
    let cellInfoList = {"ID": 0, "Table": cell.closest("section").id, "Column": ""}

    // Get column name, finds the indexOf the cell on the array of td
    const columns = (cellInfoList["Table"] === "unions") ? unions_columns : nations_columns;
    cellInfoList["Column"] = columns[Array.prototype.indexOf.call(cell.parentNode.querySelectorAll("td"), cell)];
    
    // Get row ID, finds the indexOf the row (cell.parentNode) on the array of tr, but subtract 1 for first row which is headings
    console.log(cell, cell.parentNode)
    cellInfoList["ID"] = Array.prototype.indexOf.call(cell.closest("table").querySelectorAll("tr"), cell.parentNode) - 1;

    return cellInfoList;
}

export function addUpdatedCell(cellToEdit, cellIsNew=false) {
    cellToEdit.removeAttribute("contenteditable");
    cellToEdit.removeAttribute("spellcheck");

    let cellInfoList = getCellInfo(cellToEdit)
    // if (cellIsNew) {
    //     cellInfoList["ID"] += " newCell"
    // }

    cellsEdited.set(Object.values(cellInfoList).join(" "), cellToEdit.textContent);
}

export function sendUpdatedCells(body=JSON.stringify(Object.fromEntries(cellsEdited))) {
    fetch("/stats/save", {
        method: 'PUT', 
        headers: {'Content-Type': 'application/json; charset=UTF-8'}, 
        body: body
    })
    .catch((error) => {console.error('Error:', error)});

    cellsEdited.clear();
}
