const lis = document.querySelector('#lista')

fetch('http://localhost:8000/get_lista').then((res) => {
    return res.json();

}).then ((data) => {
    data.map((lista) => {
        console.log(lista)
        lis.innerHTML +=
        `<li>
            <strong>Nome do filme:</strong> ${lista.nome} </br>
            <strong>Atores:</strong> ${lista.atores} </br>
            <strong>Diretor:</strong> ${lista.diretor} </br>
            <strong>Ano de Lançamento:</strong> ${lista.anoFilme} </br>
            <strong>Genêros:</strong> ${lista.genero} </br>
            <strong>Produtora:</strong> ${lista.produtora} </br>
            <strong>Sinopse:</strong> ${lista.sinopse} </br>
        </li>
        <button type="submit" value="deletar">DELETAR</button>
        <button type="submit" value="editar">EDITAR</button>
        `
    })
})