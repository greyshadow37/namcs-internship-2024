import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:5000';

export const fetchPrediction = async (params) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/predict`, params);
    return response.data;
  } catch (error) {
    if (error.response) {
      // The request was made, and the server responded with a status code
      // that falls out of the range of 2xx
      console.error('Server responded with an error:', error.response.data);
      throw new Error(error.response.data.error || 'Server Error');
    } else if (error.request) {
      // The request was made, but no response was received
      console.error('No response received:', error.request);
      throw new Error('No response from server. Please try again later.');
    } else {
      // Something happened in setting up the request that triggered an Error
      console.error('Error setting up request:', error.message);
      throw new Error('Error in setting up request. Please try again.');
    }
  }
};
