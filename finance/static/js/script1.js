function calculateAdvice() {
    const income = parseFloat(document.getElementById("income").value);
    const expenses = parseFloat(document.getElementById("expenses").value);
    const savings = parseFloat(document.getElementById("savings").value);

    if (isNaN(income) || isNaN(expenses) || isNaN(savings)) {
        document.getElementById("advice").innerText = "Please enter valid numbers.";
        return;
    }

    const discretionaryIncome = income - expenses;
    let advice = "";

    if (discretionaryIncome < savings) {
        advice = "You should consider reducing your expenses or increasing your income.";
    } else if (discretionaryIncome >= savings) {
        advice = "Great job! You are on track to meet your savings goal.";
    }

    document.getElementById("advice").innerText = advice;
}

