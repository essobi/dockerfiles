FROM ubuntu:14.04  
MAINTAINER Yu Shi <tttptd@yandex.com>  
  
RUN sudo apt-get -y update && \  
sudo apt-get -y install python-software-properties software-properties-common
python-setuptools && \  
sudo add-apt-repository ppa:yandex-load/main && \  
sudo apt-get -y update && \  
sudo apt-get -y install yandex-tank  
  
ADD ./tank.ini /tank/load.ini  
CMD ["yandex-tank"]  
WORKDIR /tank  

