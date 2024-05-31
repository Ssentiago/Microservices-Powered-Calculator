let display = document.getElementById("display");

const API = "http://127.0.0.1:8000"

function addEventNumber() {
    numbers = document.querySelectorAll(".btn-number");
    numbers.forEach(number => {
        number.addEventListener("click", function () {
            if (!display.textContent.match(/=/)) {
                console.log(this.textContent)
                if (this.textContent.match(/\./)) {
                    if (display.textContent !== "0") {
                        let check = display.textContent.split(/[÷+×-]/)
                        if (check.pop().match(/^\d+$/)) {
                            display.textContent += this.textContent
                        }
                    }
                }
                if (this.textContent.match(/\d/)) {
                    if (display.textContent === "0") {
                        display.textContent = "";
                        display.textContent += this.textContent
                    } else {
                        display.textContent += this.textContent;
                    }
                }
            } else {
                if (this.textContent.match(/\d/)) {
                    display.textContent = this.textContent;
                }
            }
        })
    })
}

function addEventOperators() {
    ops = document.querySelectorAll(".btn-operator");
    ops.forEach(op => {
        op.addEventListener("click", function () {
            if (!display.textContent.match(/=/)) {
                last = display.textContent.charAt(display.textContent.length - 1)
                console.log(last)
                if (!last.match(/[+×÷-]/)) {
                    display.textContent += this.textContent;
                }
            } else {
                display.textContent = "0"
            }


        })
    })
}


function addEventClear() {
    clear_b = document.getElementById("clear")
    clear_b.addEventListener("click", function () {
        display.textContent = "0";
    })
}

function addEventEvaluate() {
    el = document.getElementById("evaluate");
    el.addEventListener("click", async function () {
        if (!display.textContent.match(/=/)) {
            const response = await fetch(`${API}/calculate`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    expr: display.textContent
                })
            })

            if (response.status === 200) {
                const data = await response.json();
                display.textContent += "=" + data.result;
            }
        } else {
            display.textContent = "0";
        }

    })


}

async function addButtonListeners() {
    addEventNumber()
    addEventOperators()
    addEventClear()
    addEventEvaluate()
}