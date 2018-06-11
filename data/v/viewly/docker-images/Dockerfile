FROM ubuntu:17.10  
RUN apt update && apt upgrade -y  
RUN apt install -y git tar ssh gzip ca-certificates sudo  
RUN apt install -y pkg-config dh-autoreconf  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
RUN apt install -y libffi-dev libssl-dev python3 python3-dev python3-pip  
  
RUN apt install software-properties-common -y  
RUN add-apt-repository ppa:ethereum/ethereum  
RUN apt update && apt install solc -y  
  
RUN pip3 install pipenv  
RUN pip3 install secp256k1  

