const lis = document.querySelector('#lista')

fetch('http://localhost:8000/get_lista')
  .then((res) => res.json())
  .then((data) => {
    lis.innerHTML = ''; 

    data.forEach((filme) => {
      const li = document.createElement('li');
      li.innerHTML = `
        <strong>Nome do filme:</strong> ${filme.nome} </br>
        <strong>Atores:</strong> ${filme.atores} </br>
        <strong>Diretor:</strong> ${filme.diretor} </br>
        <strong>Ano de Lançamento:</strong> ${filme.anoFilme} </br>
        <strong>Gêneros:</strong> ${filme.genero} </br>
        <strong>Produtora:</strong> ${filme.produtora} </br>
        <strong>Sinopse:</strong> ${filme.sinopse} </br>
        <button class="btn-deletar" data-id="${filme.id}">Deletar</button>
        <button class="btn-editar" data-id="${filme.id}">Editar</button>
        <hr/>
      `;
      lis.appendChild(li);
    });
  });

document.querySelector('#lista').addEventListener('click', function (e) {
  const id = e.target.dataset.id;

  if (!id) return;

  if (e.target.classList.contains('btn-deletar')) {
    fetch(`http://localhost:8000/send_delete/${id}`, {
      method: 'DELETE',
    })
      .then((res) => {
        if (res.ok) {
          alert('Filme deletado com sucesso!');
          location.reload();
        } else {
          alert('Erro ao deletar filme.');
        }
      });
  }

  if (e.target.classList.contains('btn-editar')) {
    const novoNome = prompt('Digite o novo nome do filme:');
    if (!novoNome) return;

    fetch(`http://localhost:8000/send_edit/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ nome: novoNome })
    })
      .then((res) => {
        if (res.ok) {
          alert('Filme atualizado com sucesso!');
          location.reload();
        } else {
          alert('Erro ao editar filme.');
        }
      });
  }
});
