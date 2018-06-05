FROM ubuntu:xenial  
  
RUN apt-get update  
  
RUN apt-get install -y build-essential python python-pip git wget curl nano
make g++  
  
RUN apt-get install -y libboost-all-dev libtag1-dev zlib1g-dev  
  
RUN apt-get install -y ffmpeg  
  
RUN mkdir /opt/echoprint && \  
cd /opt/echoprint && \  
git clone \--depth=1 https://github.com/spotify/echoprint-codegen.git codegen
&& \  
git clone \--depth=1 https://github.com/spotify/echoprint-server.git server  
  
WORKDIR /opt/echoprint  
  
RUN cd codegen/src && \  
make && \  
mv ../echoprint-codegen /usr/local/bin/echoprint-codegen  
  
RUN cd server && \  
python setup.py install && \  
pip install nose flake8 flask tornado  
  
RUN apt-get remove -y build-essential g++ python-pip && \  
apt-get autoremove -y && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

