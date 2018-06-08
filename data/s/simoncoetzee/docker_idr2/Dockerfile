FROM ubuntu:14.04  
MAINTAINER Simon Coetzee "simon.coetzee@cshs.org"  
ENV DEBIAN_FRONTEND noninteractive  
### utilities  
RUN apt-get update &&\  
apt-get -y upgrade && \  
apt-get install -y bedtools \  
build-essential \  
gfortran \  
git \  
libopenblas-base \  
libopenblas-dev \  
liblapack3 \  
liblapack-dev \  
python3 \  
python3-pip \  
python3-dev \  
pkg-config \  
libfreetype6-dev  
  
### idr2  
RUN pip3 install numpy  
RUN pip3 install matplotlib  
RUN pip3 install scipy  
#RUN wget https://github.com/nboley/idr/archive/2.0.2.zip && mv 2.0.2.zip
~/idr2.zip  
#RUN unzip ~/idr2.zip -d /root/ && cd ~/idr-2.0.2/ && python3 setup.py install  
RUN git clone https://github.com/Simon-Coetzee/idr && cd idr && \  
python3 setup.py install  
  
COPY run.spp.sh /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
CMD ["run"]  
  
VOLUME /data  

