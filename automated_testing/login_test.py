{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1872cc10",
   "metadata": {},
   "outputs": [
    {
     "ename": "",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31mRunning cells with 'Python 3.12.3' requires the ipykernel package.\n",
      "\u001b[1;31mInstall 'ipykernel' into the Python environment. \n",
      "\u001b[1;31mCommand: '/usr/bin/python3 -m pip install ipykernel -U --user --force-reinstall'"
     ]
    }
   ],
   "source": [
    "import time\n",
    "import os\n",
    "\n",
    "# Install Chrome browser and necessary dependencies\n",
    "!apt-get update\n",
    "!apt-get install -y fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgbm1 libgcc1 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 xdg-utils\n",
    "!wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb\n",
    "!dpkg -i google-chrome-stable_current_amd64.deb\n",
    "!apt-get install -f # Fix broken dependencies\n",
    "\n",
    "!pip install selenium webdriver-manager\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.by import By\n",
    "from selenium.webdriver.chrome.service import Service\n",
    "from selenium.webdriver.chrome.options import Options\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "\n",
    "# Launch browser\n",
    "options = Options()\n",
    "options.add_argument('--headless')\n",
    "options.add_argument('--no-sandbox')\n",
    "options.add_argument('--disable-dev-shm-usage')\n",
    "options.binary_location = '/usr/bin/google-chrome' # Specify the path to google-chrome\n",
    "driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)\n",
    "\n",
    "def test_login(username, password):\n",
    "    driver.get('https://the-internet.herokuapp.com/login')\n",
    "    driver.find_element(By.ID, 'username').send_keys(username)\n",
    "    driver.find_element(By.ID, 'password').send_keys(password)\n",
    "    driver.find_element(By.CSS_SELECTOR, 'button[type=\"submit\"]').click()\n",
    "    time.sleep(1)\n",
    "    page_text = driver.page_source.lower()\n",
    "    if \"you logged into a secure area!\" in page_text:\n",
    "        result = \"Success\"\n",
    "    elif \"your username is invalid!\" in page_text:\n",
    "        result = \"Failure\"\n",
    "    else:\n",
    "        result = \"Unknown\"\n",
    "    driver.save_screenshot(f\"login_{username}_{result}.png\")\n",
    "    return result\n",
    "\n",
    "\n",
    "# Valid credentials (provided by demo site)\n",
    "valid_user = \"tomsmith\"\n",
    "valid_pass = \"SuperSecretPassword!\"\n",
    "\n",
    "# Valid Login Test\n",
    "print(\"Valid login:\", test_login(valid_user, valid_pass))\n",
    "# Invalid Login Test\n",
    "print(\"Invalid login:\", test_login(\"wronguser\", \"badpassword\"))\n",
    "\n",
    "driver.quit()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
