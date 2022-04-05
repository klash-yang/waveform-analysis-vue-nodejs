const axios = require('axios');

export const dataRequest = async () => {
  try {
    const response = await axios.get('http://localhost:3000/');
    return response
  } catch (error) {
    console.error(error)
  }
}
