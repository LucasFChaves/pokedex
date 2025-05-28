import React from 'react';

function PokemonRow({ pokemon, onDelete }) {
  const { codigo, nome, tipoPrimario, tipoSecundario } = pokemon;

  return (
    <tr>
      <td>{codigo}</td>
      <td>{nome}</td>
      <td>{tipoPrimario}</td>
      <td>{tipoSecundario}</td>
      <td>
        <button onClick={() => alert(`Editar ${nome}`)}>Editar</button>
        <button onClick={() => onDelete(codigo)}>Excluir</button>
      </td>
    </tr>
  );
}

export default PokemonRow;
