$(document).ready(function() {
    $('.edit-btn').on('click', function() {
        var id = $(this).data('id');
        $.ajax({
            url: '/cliente/' + id,
            method: 'GET',
            success: function(data) {
                $('#edit-id-clienteform').val(data.id);
                $('#edit-cliente-clienteform').val(data.nome);
                $('#edit-endereco-clienteform').val(data.endereco);
                $('#edit-numero_endereco-clienteform').val(data.numero);
                $('#edit-cidade-clienteform').val(data.cidade);
                $('#edit-cep-clienteform').val(data.cep);
                $('#edit-estado-clienteform').val(data.estado);
                $('#edit-documento-clienteform').val(data.documento);
                $('#edit-email-clienteform').val(data.email);
                $('#edit-fone-clienteform').val(data.telefone);
                $('#editModal').css('display', 'block');
            }
        });
    });

    $('.close-btn').on('click', function() {
        $('#editModal').css('display', 'none');
    });

    $(window).on('click', function(event) {
        if (event.target == $('#editModal')[0]) {
            $('#editModal').css('display', 'none');
        }
    });
});