FROM python:3.6  
  
# Set up code directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install Linux dependencies  
RUN apt-get update && apt-get install -y libssl-dev \  
&& apt install -y netcat-openbsd \  
&& git clone https://github.com/ethereum/web3.py.git ./ \  
&& git checkout tags/v4.2.1 \  
&& echo amqpy >> requirements-dev.txt \  
&& echo py-solc >> requirements-dev.txt \  
&& pip install -r requirements-dev.txt \  
&& pip install -e . \  
&& python -m solc.install v0.4.19 \  
&& ln -s $HOME/.py-solc/solc-v0.4.19/bin/solc /usr/local/bin/solc  
  
WORKDIR /app  

