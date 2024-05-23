import React, { useState, useEffect } from 'react';
import axios from 'axios';

function MessageComponent() {
    const [message, setMessage] = useState('');

    useEffect(() => {
        const fetchData = async () => {
            const response = await axios.get('http://localhost:5000/get-message');
            setMessage(response.data.message);
        };

        fetchData();
    }, []);

    return (
        <div>
            <h1>{message}</h1>
        </div>
    );
}

export default MessageComponent;
