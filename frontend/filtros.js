import React from 'react';

function Filters({ filterName, setFilterName, filterType, setFilterType }) {
  return (
    <div style={{ marginBottom: '20px' }}>
      <input
        type="text"
        placeholder="Buscar por nome..."
        value={filterName}
        onChange={(e) => setFilterName(e.target.value)}
      />
      <select value={filterType} onChange={(e) => setFilterType(e.target.value)}>
        <option value="">Todos os Tipos</option>
        <option value="Grass">Grass</option>
        <option value="Fire">Fire</option>
        <option value="Water">Water</option>
        <option value="Poison">Poison</option>
        <option value="Normal">Normal</option>
        <option value="Fighting">Fighting</option>
        <option value="Electric">Electric</option>
        <option value="Ice">Ice</option>
        <option value="Ground">Ground</option>
        <option value="Flying">Flying</option>
        <option value="Psychic">Psychic</option>
        <option value="Bug">Bug</option>
        <option value="Rock">Rock</option>
        <option value="Ghost">Ghost</option>
        <option value="Dragon">Dragon</option>
        <option value="Steel">Steel</option>
      </select>
    </div>
  );
}

export default Filters;
