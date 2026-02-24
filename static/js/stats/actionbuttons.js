import {rowSelectInfo, sendUpdatedCells} from './globals.js';

export function activateDeleteOrPaintButtons(event) {
    let popup = document.querySelector("#action-instructions")
    const buttonPressed = event.target.closest(".button-pill")

    if (popup.style.display !== "block" || rowSelectInfo["type"] !== buttonPressed.id) {
        popup.style.display = "block";
        rowSelectInfo["mode"] = true;
        rowSelectInfo["type"] = buttonPressed.id

        if (buttonPressed.id === "delete-row") {
            document.querySelector("#repaint").style.display = "none";
            popup.textContent = "Click on a row to delete it."
            
        } else if (buttonPressed.id === "paint-row") {
            popup.textContent = "Click on a row to change its background color."
        }
    } else {
        popup.style.display = "none";
        rowSelectInfo["mode"] = false;
    }
}

export function selectionUIMode(table) {
    table.addEventListener("mouseenter", function(event) {
        if (rowSelectInfo["mode"] && event.target.tagName === "TD") {
            if (rowSelectInfo["type"] === "delete-row" || event.target.closest("section").id === "nations") {
                event.target.parentNode.classList.add("row-selection-mode");
            }
        }
    }, true);

    table.addEventListener("mouseleave", function(event) {
        if (rowSelectInfo["mode"] && event.target.tagName === "TD") {
            event.target.parentNode.classList.remove("row-selection-mode");
        }
    }, true);
}

export function deleteOrPaintRows(rowClicked, cellInfoList) {
    document.querySelector("#action-instructions").style.display = "none";

    rowClicked.classList.remove("row-selection-mode");
    rowSelectInfo["mode"] = false;

    if (rowSelectInfo["type"] === "delete-row") {
        fetch(`/stats/delete/${cellInfoList["Table"]}/${cellInfoList["ID"]}`, {method: 'DELETE'})
        rowClicked.remove()
    } else if (rowClicked.closest("section").id === "nations") {
        document.querySelector("#repaint").style.display = "block";

        document.querySelector("#repaint-submit").addEventListener("click", function() {
            document.querySelector("#repaint").style.display = "none";

            const submittedHexValue = document.querySelector("#repaint-hex").value
            rowClicked.style.backgroundColor = `#${submittedHexValue}`
            
            sendUpdatedCells(`{"${cellInfoList["ID"]} Nations Background": "#${submittedHexValue}"}`);

        }, {once: true})

        document.querySelector("#repaint-cancel").addEventListener("click", function() {
            document.querySelector("#repaint").style.display = "none";
        }, {once: true})
    } else {
        document.querySelector("#action-instructions").style.display = "block";
        rowSelectInfo["mode"] = true;
    }
}