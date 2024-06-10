$(document).ready(function() {
    // Seleciona o elemento <select> e <input> com jQuery
    const selectDocumento = $('#label-documento select');
    const inputDocumento = $('#documento-clienteform');

    // Define o valor inicial do <select> como 'CPF'

    // Adiciona um evento de mudança ao <select> usando jQuery
    selectDocumento.on('change', function() {
        // Obtém o valor selecionado no <select>
        const selectedOption = selectDocumento.val();

        // Define a máscara e o placeholder com base na opção selecionada
        if (selectedOption === 'CPF') {
            inputDocumento.mask('000.000.000-00'); // Aplica a máscara para CPF
            inputDocumento.attr('placeholder', '000.000.000-00'); // Define o placeholder para CPF
            inputDocumento.prop('disabled', false); // Habilita o campo
        } else if (selectedOption === 'CNPJ') {
            inputDocumento.mask('00.000.000/0000-00'); // Aplica a máscara para CNPJ
            inputDocumento.attr('placeholder', '00.000.000/0000-00'); // Define o placeholder para CNPJ
            inputDocumento.prop('disabled', false); // Habilita o campo
        } else if (selectedOption === 'Docnull') {
            inputDocumento.attr('placeholder', 'Selecione um Documento');
            inputDocumento.prop('disabled', true); // Desabilita o campo
        }
    });
});

