import unittest
from unittest.mock import patch, mock_open, MagicMock
import base64
from client import encode_image, create_output 

# Class to test the two functions in the client.py program 
class TestFunctions(unittest.TestCase):
    def test_encode_image(self):
        mock_image_data = b"image"
        encoded_image_data = base64.b64encode(mock_image_data).decode('utf-8')

        with patch("builtins.open", mock_open(read_data=mock_image_data)) as mock_file:
            result = encode_image("fake_image_path.jpg")
            mock_file.assert_called_once_with("fake_image_path.jpg", 'rb')
            self.assertEqual(result, encoded_image_data)

    """
    @patch('requests.post')
    def test_create_output(self, mock_post):
        pass
    """
   


if __name__ == '__main__':
    unittest.main()