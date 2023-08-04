import React, {useState} from 'react';

function CocktailInfo({cocktail}) {
    const [showInstruction, setShowInstruction] = useState(false);

    const toggleInstruction = () => {
        setShowInstruction(!showInstruction);
    };

    return (
        <div>
            <h1>{cocktail.Name}</h1>
            <p>{cocktail.Category}</p>
            <img src={cocktail.Photo} alt="Cocktail Image" className="cocktail-image"/>
            <h2>Instruction:</h2>
            <p className="instruction"
               style={{display: showInstruction ? 'block' : 'none', padding: '0 250px'}}>{cocktail.Instruction}</p>
            <button onClick={toggleInstruction}>Toggle Instruction</button>
            <h2>Ingredients:</h2>
            <ul>
                {cocktail.Ingredients.map((ingredient, index) => (
                    <li key={index}>{ingredient}</li>
                ))}
            </ul>
        </div>
    );
}

export default CocktailInfo;