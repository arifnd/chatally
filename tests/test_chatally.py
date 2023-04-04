import os
import unittest
from unittest.mock import patch
from chatally import generate_message


class ChatAllyTestCase(unittest.TestCase):
    @patch.dict(os.environ, {'OPENAI_API_KEY': 'fake_key'})
    def test_generate_message(self):
        message_text = "Hello, how are you?"
        expected_response = "I'm doing well, thank you for asking. How can I assist you today? [CHAT GPT]"

        with patch('openai.Completion.create') as mock_create:
            mock_create.return_value.choices[0].text = expected_response
            response = generate_message(message_text)

        mock_create.assert_called_once_with(
            engine='text-davinci-002',
            prompt=f"{message_text.strip()} [CHAT GPT]",
            max_tokens=60,
            n=1,
            stop='',
            temperature=0.7,
        )
        self.assertEqual(response, expected_response)


if __name__ == '__main__':
    unittest.main()
