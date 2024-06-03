window.onload = function() {
    const cliente = {
        id: '{{ cliente[0] }}',
        nome: '{{ cliente[1] }}',
        endereco: '{{ cliente[2] }}',
        numero: '{{ cliente[3] }}',
        cidade: '{{ cliente[4] }}',
        cep: '{{ cliente[5] }}',
        estado: '{{ cliente[6] }}',
        documento: '{{ cliente[7] }}',
        email: '{{ cliente[8] }}',
        telefone: '{{ cliente[9] }}'
        // Adicione outros campos conforme necessário
    };

    // Preencher os campos do formulário com os dados do cliente
    document.getElementById('cliente-clienteform').value = cliente.nome;
    document.getElementById('endereco-clienteform').value = cliente.endereco;
    document.getElementById('numero_endereco-clienteform').value = cliente.numero;
    document.getElementById('cidade-clienteform').value = cliente.cidade;
    document.getElementById('cep-clienteform').value = cliente.cep;
    document.getElementById('estado-clienteform').value = cliente.estado;
    document.getElementById('documento-clienteform').value = cliente.documento;
    document.getElementById('email-clienteform').value = cliente.email;
    document.getElementById('fone-clienteform').value = cliente.telefone;
    // Preencha outros campos conforme necessário
};
