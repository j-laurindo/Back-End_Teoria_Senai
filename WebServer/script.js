const lis = document.querySelector('#lista');

fetch('http://localhost:8000/get_filmes')
  .then((res) => res.json())
  .then((data) => {
    lis.innerHTML = ''; 

    data.forEach((filme) => {
      const li = document.createElement('li');
      li.innerHTML = `
        <strong>Título:</strong> ${filme.titulo} <br>
        <strong>Orçamento:</strong> ${filme.orcamento} <br>
        <strong>Duração:</strong> ${filme.duracao} min<br>
        <strong>Ano de Lançamento:</strong> ${filme.ano} <br>
        <strong>Poster:</strong><br>
        <img src="${filme.poster}" alt="Poster de ${filme.titulo}" height="120"><br>
        <button class="btn-deletar" data-id="${filme.id_filme}">Deletar</button>
        <button class="btn-editar" data-id="${filme.id_filme}">Editar</button>
        <hr/>
      `;
      lis.appendChild(li);
    });
  })
  .catch((error) => {
    console.error('Erro ao carregar filmes:', error);
    lis.innerHTML = '<p>Erro ao carregar filmes.</p>';
  });
