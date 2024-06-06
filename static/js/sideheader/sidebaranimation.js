// Função para alternar a barra lateral e o main
function toggleSidebar() {
    var sidebar = document.getElementById('sidebar');
    var mains = document.querySelectorAll('main');
  
    if (sidebar.classList.contains('close-sidebar')) {
        // Se a barra lateral estiver fechada, abre ela
        sidebar.classList.remove('close-sidebar');
        sidebar.classList.add('open-state');
        mains.forEach(function(main) {
            main.classList.remove('close-sidebar');
            main.classList.add('open-state');
        });
    } else {
        // Se a barra lateral estiver aberta, fecha ela
        sidebar.classList.remove('open-state');
        sidebar.classList.add('close-sidebar');
        mains.forEach(function(main) {
            main.classList.remove('open-state');
            main.classList.add('close-sidebar');
        });
    }
  }
  
  // Adiciona o evento de clique ao botão da barra lateral
  document.getElementById('sidebar_button').addEventListener('click', toggleSidebar);
  
  // Verifica se existe um estado salvo para a barra lateral e o main ao carregar a página
  document.addEventListener('DOMContentLoaded', function() {
    var sidebar = document.getElementById('sidebar');
    var mains = document.querySelectorAll('main');
  
    // Verifica se existe um estado salvo para a barra lateral
    if (localStorage.getItem('sidebarState') === 'closed') {
        sidebar.classList.add('close-sidebar');
        mains.forEach(function(main) {
            main.classList.add('close-sidebar');
        });
    }
  });
  
  // Salva o estado da barra lateral ao sair da página
  window.addEventListener('beforeunload', function() {
    var sidebar = document.getElementById('sidebar');
  
    // Salva o estado da barra lateral no armazenamento local do navegador
    if (sidebar.classList.contains('close-sidebar')) {
        localStorage.setItem('sidebarState', 'closed');
    } else {
        localStorage.setItem('sidebarState', 'open');
    }
  });