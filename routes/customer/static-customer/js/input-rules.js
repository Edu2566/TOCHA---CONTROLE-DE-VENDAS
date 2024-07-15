$(document).ready(function() {
    // Select the <select> and <input> elements using jQuery
    const selectDocument = $('#label-document select');
    const inputDocument = $('#document-customerform');

    // Set the initial value of <select> to 'CPF'

    // Add a change event to the <select> using jQuery
    selectDocument.on('change', function() {
        // Get the selected value from <select>
        const selectedOption = selectDocument.val();

        // Set mask and placeholder based on the selected option
        if (selectedOption === 'CPF') {
            inputDocument.mask('000.000.000-00'); // Apply CPF mask
            inputDocument.attr('placeholder', '000.000.000-00'); // Set CPF placeholder
            inputDocument.prop('disabled', false); // Enable the input field
        } else if (selectedOption === 'CNPJ') {
            inputDocument.mask('00.000.000/0000-00'); // Apply CNPJ mask
            inputDocument.attr('placeholder', '00.000.000/0000-00'); // Set CNPJ placeholder
            inputDocument.prop('disabled', false); // Enable the input field
        } else if (selectedOption === 'Docnull') {
            inputDocument.attr('placeholder', 'Select a Document');
            inputDocument.prop('disabled', true); // Disable the input field
        }
    });
});
