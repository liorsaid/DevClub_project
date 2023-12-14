import 'bootstrap';
import React, { useState } from 'react'; // *



function Params({ onSearchFlight, flightDetails }) { // *
    const [location, setLocation] = useState('');
    const [destination, setDestination] = useState('');
    const [date, setDate] = useState('');

    const handleSearch = () => {
        onSearchFlight(location, destination, date);
    };

    return (
        <div>
            <form>
                <div style={{marginBottom: '5px'}}>
                    <label style={{display: 'block'}}>Enter your Location:
                        <input type="text" value={location} onChange={(e) => setLocation(e.target.value)}/>
                    </label>
                </div>
                <div style={{marginBottom: '5px'}}>
                    <label style={{display: 'block'}}>Enter your Destination:
                        <input type="text" value={destination} onChange={(e) => setDestination(e.target.value)}/>
                    </label>
                </div>
                <div style={{marginBottom: '5px'}}>
                    <label style={{display: 'block'}}>Enter the flight's date:
                        <input type="text" value={date} onChange={(e) => setDate(e.target.value)}/>
                    </label>
                </div>
                <button type="button" onClick={handleSearch}>Search Flight</button>
            </form>

            {/* Render flight details if available */}
            {flightDetails && (
                <div>
                    <h2>Flight Details are:</h2>
                    <pre>{JSON.stringify(flightDetails, null, 2)}</pre>
                    {/* Add other flight details here */}
                </div>
            )}
        </div>
    ); // *
}

export default function MyApp() { // The main component in the file

    const [flightDetails, setFlightDetails] = useState(null);
    const handleSearchFlight = (location, destination, date) => {
        console.log('Search flight:', {location, destination, date});
        const url = `http://127.0.0.1:5000/get_flight_offers?location=${location}&destination=${destination}&date=${date}`;
        // * console.log -
        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok.');
                }
                return response.json();
            })
            .then(data => {
                // Update flight details in the state
                setFlightDetails(data);
            })
            .catch(error => {
                // Handle errors
                console.error('There was a problem with the fetch operation:', error);
            });
    };


    return (
        <div>
            <h1>Are you ready for your next vacation?</h1>
            <Params onSearchFlight={handleSearchFlight} flightDetails={flightDetails}/>
        </div>
    );
}


