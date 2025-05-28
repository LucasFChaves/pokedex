import React from 'react';
import PokemonRow from './PokemonRow';

function PokemonTable({ pokemons, onDelete }) {
  return (
    <table border="1" width="100%">
      <thead>
        <tr>
          <th>Código</th>
          <th>Nome</th>
          <th>Tipo Primário</th>
          <th>Tipo Secundário</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        {pokemons.map(pokemon => (
          <PokemonRow key={pokemon.codigo} pokemon={pokemon} onDelete={onDelete} />
        ))}
      </tbody>
    </table>
  );
}

export default PokemonTable;
