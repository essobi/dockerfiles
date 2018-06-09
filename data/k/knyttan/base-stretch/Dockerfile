FROM debian:stretch  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-transport-https \  
build-essential \  
curl \  
gosu \  
gnupg2 \  
gettext \  
ipython3 \  
pngquant \  
python3 \  
python3-crypto \  
python3-cryptography \  
python3-ipdb \  
python3-lxml \  
python3-pil \  
python3-pip \  
python3-psycopg2 \  
python3-scipy \  
python3-setuptools \  
python3-software-properties \  
python3-wheel  
  
RUN pip3 install --upgrade safety boto3 docopt  
ADD safety.sh /usr/local/bin/safety.sh  
ADD get_secrets.py /usr/local/bin/get_secrets.py  

