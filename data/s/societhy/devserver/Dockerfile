# base image is debian  
FROM ubuntu:latest  
  
RUN apt-get update && \  
apt-get upgrade -qy && \  
apt-get dist-upgrade -qy && \  
apt-get update --fix-missing && \  
apt-get install software-properties-common -qy  
  
RUN add-apt-repository -y ppa:ethereum/ethereum && \  
add-apt-repository -y ppa:ethereum/ethereum-dev && \  
add-apt-repository -y ppa:jonathonf/python-3.6 && \  
apt-get update -y  
  
ENV DEPENDENCIES="python3.6 python3.6-dev autoconf autogen intltool libtool
libffi-dev golang python3-pip python-virtualenv libssl-dev curl file binutils
make git tmux colord zsh ethminer npm nodejs inetutils-ping solc pkg-config
mongodb supervisor ethereum wget redis-server"  
RUN apt-get install $DEPENDENCIES -qy  
  
RUN apt-get install libffi-dev  
  
COPY ./utils/parity_bin /usr/local/bin/parity  
  
#RUN bash /install_parity.sh  
RUN python3.6 -m pip install --upgrade pip  
  
COPY ./utils/requirements.txt /societhy/requirements.txt  
  
RUN pip3.6 install -r /societhy/requirements.txt --upgrade  
  
RUN pip3.6 install -e
git+https://github.com/simonvadee/ethjsonrpc#egg=ethjsonrpc  
  
RUN pip3.6 install -e git+https://github.com/simonvadee/mongokat#egg=mongokat  
  
ENV HOME="/societhy"  
WORKDIR /societhy  
  
COPY ./utils/ /societhy/utils  
  
RUN echo 'alias run="python3.6 app/app.py"' >> ~/.zshrc  
  
RUN echo 'alias console="geth attach rpc:http://172.17.0.2:8545"' >> ~/.zshrc  
  
EXPOSE 8080  
EXPOSE 22

