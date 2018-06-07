FROM ubuntu:16.04  
RUN \  
apt-get -y update && \  
apt-get install -y python && \  
apt-get install -y python-setuptools python-dev build-essential wget && \  
wget http://curl.haxx.se/ca/cacert.pem && \  
mv cacert.pem ca-bundle.crt && \  
mv ca-bundle.crt /usr/local/share/ca-certificates/ && \  
update-ca-certificates && \  
easy_install pip && \  
pip install \--upgrade pip && \  
pip install selenium \--user && \  
pip install slacker \--user && \  
pip install redis \--user && \  
pip install python-digitalocean \--user && \  
pip install uuid \--user && \  
pip install requests \--user && \  
pip install vultr \--user  
WORKDIR /happyfeet  
COPY happyfeet.py /happyfeet  
CMD ["python", "/happyfeet/happyfeet.py", "start"]  

