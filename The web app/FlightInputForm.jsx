import React, { useState } from 'react';
import axios from 'axios'; // Import axios


const FlightInputForm = ({ onSearch }) => {
    const [source, setSource] = useState('');
    const [destination, setDestination] = useState('');
    const [date, setDate] = useState('');


    const handleSubmit = async (event) => {
        //event.preventDefault(); // Prevent the default form submission behavior

        try {
            // Make an API request to my Python server
            const response = await axios.get('/search-flight', {
                params: { source, destination, date } // Pass user input as query parameters
            });
            // Pass the search results to the parent component
            onSearch(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div>
            <h2>Flight Search</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="source">Source:</label>
                    <input
                        type="text"
                        id="source"
                        value={source}
                        onChange={(event) => setSource(event.target.value)}
                    />
                </div>
                <div>
                    <label htmlFor="destination">Destination:</label>
                    <input
                        type="text"
                        id="destination"
                        value={destination}
                        onChange={(event) => setDestination(event.target.value)}
                    />
                </div>
                <div>
                    <label htmlFor="date">Date:</label>
                    <input
                        type="date"
                        id="date"
                        value={date}
                        onChange={(event) => setDate(event.target.value)}
                    />
                </div>
                <button type="submit">Search</button>
            </form>
        </div>
    );
};

export default FlightInputForm;