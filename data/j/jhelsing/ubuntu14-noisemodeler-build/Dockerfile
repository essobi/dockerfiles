FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y \  
g++ \  
git \  
libboost-signals-dev \  
libqt5svg5-dev \  
make \  
qt5-default \  
qtdeclarative5-dev \  
vim  
COPY ./build-latest-noisemodeler.sh /  
VOLUME /var/jenkins_home  
ENTRYPOINT ["/build-latest-noisemodeler.sh"]  

