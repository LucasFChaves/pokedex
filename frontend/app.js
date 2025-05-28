import React, { useState } from 'react';
import pokemonsData from './backend/pokemons.json';
import PokemonTable from './components/PokemonTable';
import Filters from './components/Filters';
import HeaderActions from './components/HeaderActions';

function App() {
  const [pokemons, setPokemons] = useState(pokemonsData);
  const [filterName, setFilterName] = useState('');
  const [filterType, setFilterType] = useState('');

  const filteredPokemons = pokemons.filter(p => 
    p.nome.toLowerCase().includes(filterName.toLowerCase()) &&
    (filterType === '' || p.tipoPrimario === filterType || p.tipoSecundario === filterType)
  );

  const deletePokemon = (codigo) => {
    setPokemons(prev => prev.filter(p => p.codigo !== codigo));
  };

  return (
    <div>
      <HeaderActions />
      <Filters
        filterName={filterName}
        setFilterName={setFilterName}
        filterType={filterType}
        setFilterType={setFilterType}
      />
      <PokemonTable pokemons={filteredPokemons} onDelete={deletePokemon} />
    </div>
  );
}

export default App;
