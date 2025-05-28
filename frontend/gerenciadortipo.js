import React, { useState } from 'react';

const tiposIniciais = [
  'Grass', 'Fire', 'Water', 'Electric', 'Normal', 'Poison', 'Bug',
  'Flying', 'Ground', 'Rock', 'Psychic', 'Ice', 'Ghost', 'Dragon', 'Steel'
];

function TypeManager() {
  const [tipos, setTipos] = useState(tiposIniciais);
  const [novoTipo, setNovoTipo] = useState('');
  const [editandoIndex, setEditandoIndex] = useState(null);
  const [editandoNome, setEditandoNome] = useState('');

  const adicionarTipo = () => {
    if (novoTipo && !tipos.includes(novoTipo)) {
      setTipos([...tipos, novoTipo]);
      setNovoTipo('');
    }
  };

  const excluirTipo = (index) => {
    if (window.confirm("Tem certeza que deseja excluir esse tipo?")) {
      setTipos(tipos.filter((_, i) => i !== index));
    }
  };

  const iniciarEdicao = (index) => {
    setEditandoIndex(index);
    setEditandoNome(tipos[index]);
  };

  const salvarEdicao = () => {
    const novosTipos = [...tipos];
    novosTipos[editandoIndex] = editandoNome;
    setTipos(novosTipos);
    setEditandoIndex(null);
    setEditandoNome('');
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>Gerenciar Tipos de Pokémon</h2>

      <div>
        <input
          type="text"
          placeholder="Novo tipo"
          value={novoTipo}
          onChange={(e) => setNovoTipo(e.target.value)}
        />
        <button onClick={adicionarTipo}>Adicionar Tipo</button>
      </div>

      <ul>
        {tipos.map((tipo, index) => (
          <li key={index}>
            {editandoIndex === index ? (
              <>
                <input
                  value={editandoNome}
                  onChange={(e) => setEditandoNome(e.target.value)}
                />
                <button onClick={salvarEdicao}>Salvar</button>
                <button onClick={() => setEditandoIndex(null)}>Cancelar</button>
              </>
            ) : (
              <>
                {tipo}
                <button onClick={() => iniciarEdicao(index)}>Editar</button>
                <button onClick={() => excluirTipo(index)}>Excluir</button>
              </>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TypeManager;
