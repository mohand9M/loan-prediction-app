async function submitForm() {
    try {
        const loanTerm = parseInt(document.getElementById("loan_term").value);
        const loanAmount = parseInt(document.getElementById("loan_amount").value);
        const incomeAnn = parseInt(document.getElementById("income_annum").value);
        const cibilScore = parseInt(document.getElementById("cibil_score").value);
        const noOfDependents = parseInt(document.getElementById("no_of_dependents").value);
        const resAssets = parseInt(document.getElementById("residential_assets_value").value);
        const comAssets = parseInt(document.getElementById("commercial_assets_value").value);
        const luxAssets = parseInt(document.getElementById("luxury_assets_value").value);
        const bankAssets = parseInt(document.getElementById("bank_asset_value").value);

        console.log("Données envoyées au serveur :", {
            loan_term: loanTerm,
            loan_amount: loanAmount,
            income_annum: incomeAnn,
            cibil_score: cibilScore,
            no_of_dependents: noOfDependents,
            residential_assets_value: resAssets,
            commercial_assets_value: comAssets,
            luxury_assets_value: luxAssets,
            bank_asset_value: bankAssets
        });

        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                loan_term: loanTerm,
                loan_amount: loanAmount,
                income_annum: incomeAnn,
                cibil_score: cibilScore,
                no_of_dependents: noOfDependents,
                residential_assets_value: resAssets,
                commercial_assets_value: comAssets,
                luxury_assets_value: luxAssets,
                bank_asset_value: bankAssets
            })
        });

        const result = await response.json();
        console.log("Résultat du serveur :", result);

        if (result.error) {
            alert("Erreur : " + result.error);
        } else {
            document.getElementById("result").innerText = "Résultat : " + result.prediction;
        }
    } catch (error) {
        console.log("Erreur lors de l'envoi des données :", error);
    }
}
