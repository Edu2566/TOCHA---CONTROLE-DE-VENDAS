$(document).ready(function() {
    // Seleciona o elemento <select> e <input> com jQuery
    const selectDocumento = $('#label-documento select');
    const inputDocumento = $('#documento-clienteform');

    // Define o valor inicial do <select> como 'CPF'
    selectDocumento.val('CPF');

    // Aplica a máscara e o placeholder inicialmente para CPF
    inputDocumento.mask('000.000.000-00');
    inputDocumento.attr('placeholder', '000.000.000-00');

    // Adiciona um evento de mudança ao <select> usando jQuery
    selectDocumento.on('change', function() {
        // Obtém o valor selecionado no <select>
        const selectedOption = selectDocumento.val();

        // Define a máscara e o placeholder com base na opção selecionada
        if (selectedOption === 'CPF') {
            inputDocumento.mask('000.000.000-00'); // Aplica a máscara para CPF
            inputDocumento.attr('placeholder', '000.000.000-00'); // Define o placeholder para CPF
        } else if (selectedOption === 'CNPJ') {
            inputDocumento.mask('00.000.000/0000-00'); // Aplica a máscara para CNPJ
            inputDocumento.attr('placeholder', '00.000.000/0000-00'); // Define o placeholder para CNPJ
        }
    });
});


// JavaScript para ajustar o campo de número (N°) limitando a 6 caracteres numéricos
const numeroInput = document.getElementById('numero_endereco-clienteform');
numeroInput.addEventListener('input', function(event) {
    let inputValue = event.target.value;

    // Remover todos os caracteres não numéricos
    inputValue = inputValue.replace(/\D/g, '');

    // Limitar o número máximo de caracteres a 6
    inputValue = inputValue.slice(0, 6);

    event.target.value = inputValue; // Atualizar o valor no campo
});
