let cellsEdited = new Map();
export let rowSelectInfo = {"mode": false, "type": ""}

export function addUpdatedCell(cellToEdit) {
    cellToEdit.removeAttribute("contenteditable");
    cellToEdit.removeAttribute("spellcheck");

    cellsEdited.set(cellToEdit.dataset.cellinfo, cellToEdit.textContent);
}

export function sendUpdatedCells() {
    navigator.sendBeacon("/stats/save", JSON.stringify(Object.fromEntries(cellsEdited)));
    cellsEdited.clear();
}