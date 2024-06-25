{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "09d51ba1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the long URL: https://www.w3schools.com/\n",
      "Short URL: Error: 403 - {\"message\":\"FORBIDDEN\"}\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "class URLShortener:\n",
    "    def __init__(self, access_token):\n",
    "        self.access_token = access_token\n",
    "        self.base_url = \"https://api-ssl.bitly.com/v4/shorten\"\n",
    "        self.headers = {\n",
    "            \"Authorization\": f\"Bearer {self.access_token}\",\n",
    "            \"Content-Type\": \"application/json\"\n",
    "        }\n",
    "    \n",
    "    def shorten_url(self, long_url):\n",
    "        data = {\n",
    "            \"long_url\": long_url\n",
    "        }\n",
    "        \n",
    "        response = requests.post(self.base_url, json=data, headers=self.headers)\n",
    "        \n",
    "        if response.status_code == 200:\n",
    "            return response.json().get(\"link\")\n",
    "        else:\n",
    "            return f\"Error: {response.status_code} - {response.text}\"\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    access_token = \"YOUR_BITLY_ACCESS_TOKEN\"  # Replace with your actual Bitly API access token\n",
    "    url_shortener = URLShortener(access_token)\n",
    "    \n",
    "    long_url = input(\"Enter the long URL: \")\n",
    "    short_url = url_shortener.shorten_url(long_url)\n",
    "    \n",
    "    print(f\"Short URL: {short_url}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0f036daa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the long URL: python shorten_url.py\n",
      "Short URL: Error: 403 - Forbidden. Please check your API token and permissions.\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "class URLShortener:\n",
    "    def __init__(self, access_token):\n",
    "        self.access_token = access_token\n",
    "        self.base_url = \"https://api-ssl.bitly.com/v4/shorten\"\n",
    "        self.headers = {\n",
    "            \"Authorization\": f\"Bearer {self.access_token}\",\n",
    "            \"Content-Type\": \"application/json\"\n",
    "        }\n",
    "    \n",
    "    def shorten_url(self, long_url):\n",
    "        data = {\n",
    "            \"long_url\": long_url\n",
    "        }\n",
    "        \n",
    "        response = requests.post(self.base_url, json=data, headers=self.headers)\n",
    "        \n",
    "        if response.status_code == 200:\n",
    "            return response.json().get(\"link\")\n",
    "        elif response.status_code == 403:\n",
    "            return \"Error: 403 - Forbidden. Please check your API token and permissions.\"\n",
    "        else:\n",
    "            return f\"Error: {response.status_code} - {response.text}\"\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    access_token = \"YOUR_BITLY_ACCESS_TOKEN\"  # Replace with your actual Bitly API access token\n",
    "    url_shortener = URLShortener(access_token)\n",
    "    \n",
    "    long_url = input(\"Enter the long URL: \")\n",
    "    short_url = url_shortener.shorten_url(long_url)\n",
    "    \n",
    "    print(f\"Short URL: {short_url}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c6220933",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the long URL: https://www.gucci.com/us/en/\n",
      "Short URL: https://tinyurl.com/gwpowx2\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from urllib.parse import urlencode\n",
    "\n",
    "class URLShortener:\n",
    "    def __init__(self):\n",
    "        self.base_url = \"http://tinyurl.com/api-create.php\"\n",
    "    \n",
    "    def shorten_url(self, long_url):\n",
    "        try:\n",
    "            params = {'url': long_url}\n",
    "            url = self.base_url + '?' + urlencode(params)\n",
    "            response = requests.get(url)\n",
    "            \n",
    "            if response.status_code == 200:\n",
    "                return response.text.strip()\n",
    "            else:\n",
    "                return f\"Error: Unable to shorten URL. Status code: {response.status_code}\"\n",
    "        \n",
    "        except requests.RequestException as e:\n",
    "            return f\"Request error: {str(e)}\"\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    url_shortener = URLShortener()\n",
    "    \n",
    "    long_url = input(\"Enter the long URL: \")\n",
    "    short_url = url_shortener.shorten_url(long_url)\n",
    "    \n",
    "    print(f\"Short URL: {short_url}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "01e0b2c8",
   "metadata": {},
   "outputs": [
    {
     "ename": "ImportError",
     "evalue": "cannot import name 'style_from_dict' from 'prompt_toolkit.styles' (C:\\Users\\HP\\anaconda3\\lib\\site-packages\\prompt_toolkit\\styles\\__init__.py)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mImportError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_9460/1123864648.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0murllib\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mparse\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0murlencode\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mcolorama\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0minit\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mFore\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mPyInquirer\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mprompt\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mValidator\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mValidationError\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\PyInquirer\\__init__.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mprompt_toolkit\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtoken\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mToken\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 7\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mprompt_toolkit\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstyles\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mstyle_from_dict\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      8\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mprompt_toolkit\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvalidation\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mValidator\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mValidationError\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mImportError\u001b[0m: cannot import name 'style_from_dict' from 'prompt_toolkit.styles' (C:\\Users\\HP\\anaconda3\\lib\\site-packages\\prompt_toolkit\\styles\\__init__.py)"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from urllib.parse import urlencode\n",
    "from colorama import init, Fore\n",
    "from PyInquirer import prompt, Validator, ValidationError\n",
    "\n",
    "\n",
    "class URLValidator(Validator):\n",
    "    def validate(self, document):\n",
    "        try:\n",
    "            requests.get(document.text.strip())\n",
    "        except:\n",
    "            raise ValidationError(\n",
    "                message=\"Please enter a valid URL\",\n",
    "                cursor_position=len(document.text))\n",
    "\n",
    "\n",
    "class URLShortener:\n",
    "    def __init__(self):\n",
    "        self.base_url = \"http://tinyurl.com/api-create.php\"\n",
    "\n",
    "    def shorten_url(self, long_url):\n",
    "        try:\n",
    "            params = {'url': long_url}\n",
    "            url = self.base_url + '?' + urlencode(params)\n",
    "            response = requests.get(url)\n",
    "\n",
    "            if response.status_code == 200:\n",
    "                return response.text.strip()\n",
    "            else:\n",
    "                return f\"Error: Unable to shorten URL. Status code: {response.status_code}\"\n",
    "\n",
    "        except requests.RequestException as e:\n",
    "            return f\"Request error: {str(e)}\"\n",
    "\n",
    "\n",
    "def main():\n",
    "    init(autoreset=True)  # Initialize colorama for cross-platform color support\n",
    "\n",
    "    url_shortener = URLShortener()\n",
    "\n",
    "    questions = [\n",
    "        {\n",
    "            'type': 'input',\n",
    "            'name': 'long_url',\n",
    "            'message': 'Enter the long URL:',\n",
    "            'validate': URLValidator\n",
    "        }\n",
    "    ]\n",
    "\n",
    "    answers = prompt(questions)\n",
    "\n",
    "    long_url = answers['long_url'].strip()\n",
    "    short_url = url_shortener.shorten_url(long_url)\n",
    "\n",
    "    if short_url.startswith(\"Error\"):\n",
    "        print(Fore.RED + short_url)\n",
    "    else:\n",
    "        print(Fore.GREEN + f\"Short URL: {short_url}\")\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eec85840",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
