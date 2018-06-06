FROM ubuntu:16.04  
MAINTAINER Brian S. Woolstrum <brian.woolstrum@gmail.com>  
  
RUN apt-get update && apt-get install -y qt5-default gcc g++ libqt5core5a make
autoconf libtool libtool-bin pkg-config && \  
apt-get install -y libboost-dev libboost-all-dev && \  
apt-get clean  
  
WORKDIR /src  
  
ADD build.sh /bin/build.sh  
CMD ["bash", "/bin/build.sh"]  

