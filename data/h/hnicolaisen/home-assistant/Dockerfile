FROM homeassistant/home-assistant:dev  
  
MAINTAINER Henrik Nicolaisen <henrik@nicolaisen.co>  
  
RUN apt-get update  
RUN apt-get install -y jq nmap lsof apt-transport-https netcat  
RUN curl -sL https://deb.nodesource.com/setup_6.x -o nodesource_setup.sh  
RUN bash nodesource_setup.sh  
RUN apt-get install -y nodejs  
RUN npm install ps4-waker@1.4.3 -g  
  
RUN apt-get install -y --fix-missing \  
build-essential \  
cmake \  
gfortran \  
git \  
wget \  
curl \  
graphicsmagick \  
libgraphicsmagick1-dev \  
libatlas-dev \  
libavcodec-dev \  
libavformat-dev \  
libboost-all-dev \  
libgtk2.0-dev \  
libjpeg-dev \  
liblapack-dev \  
libswscale-dev \  
pkg-config \  
python3-dev \  
python3-numpy \  
software-properties-common \  
zip \  
&& apt-get clean && rm -rf /tmp/* /var/tmp/*  
  
RUN cd ~ && \  
mkdir -p dlib && \  
git clone -b 'v19.4' \--single-branch https://github.com/davisking/dlib.git
dlib/ && \  
cd dlib/ && \  
python3 setup.py install --yes  
  
EXPOSE 8123:8123  

