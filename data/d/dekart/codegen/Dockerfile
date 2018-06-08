FROM python:2.7  
MAINTAINER Dumitru  
  
LABEL description="Codegen pre-build image" version="0.0.2"  
  
RUN apt-get update && \  
apt-get install -y libboost1.55 libtag1-dev zlib1g-dev  
  
RUN echo deb http://www.deb-multimedia.org jessie main non-free >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y --force-yes deb-multimedia-keyring && \  
apt-get update && \  
apt-get install -y ffmpeg  
  
RUN pip install click pika sqlalchemy psycopg2  
  
RUN git clone https://github.com/echonest/echoprint-codegen /tmp/echoprint-
codegen && \  
cd /tmp/echoprint-codegen/src/ && \  
make && \  
mv /tmp/echoprint-codegen/echoprint-codegen /usr/bin && \  
rm -rf /tmp/echoprint-codegen  

