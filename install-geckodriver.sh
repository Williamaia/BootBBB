export GV=v0.26.0
wget "https://github.com/mozilla/geckodriver/releases/download/$GV/geckodriver-$GV-linux64.tar.gz"
tar xvzf geckodriver-$GV-linux64.tar.gz 
chmod +x geckodriver
sudo cp geckodriver /usr/local/bin/
sudo chown $USER:$USER /usr/local/bin/geckodriver

rm -rf geckodriver-$GV-linux64.tar.gz 
rm -rf geckodriver