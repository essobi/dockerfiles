FROM python:3.6  
  
  
WORKDIR /opt/build/  
  
# Install Google Chrome  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add \- && \  
sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google.list' && \  
apt-get update && \  
apt-get install -y google-chrome-stable && \  
pip install pipenv  
  

