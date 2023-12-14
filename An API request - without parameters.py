function fetchFlightOffers(location, destination, date) {
    const url = `http://127.0.0.1:5000/get_flight_offers?location=${location}&destination=${destination}&date=${date}`;

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok.');
            }
            return response.json();
        })
        .then(data => {
            // Handle the flight offers data received from the server
            console.log('Flight offers:', data);
            // Perform further operations with the flight offers data
        })
        .catch(error => {
            // Handle any errors that occur during the fetch request
            console.error('There was a problem with the fetch operation:', error);
        });
}

// Example usage:
// Replace these values with user input or from other sources
const userLocation = 'SYD';
const userDestination = 'BKK';
const userDate = '2024-01-01';

// Call the function with user-provided parameters
fetchFlightOffers(userLocation, userDestination, userDate);
