FROM ubuntu:xenial  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get install -y \  
apt-utils  
  
RUN apt-get install -y \  
build-essential \  
perl \  
python3 \  
python3-dev \  
python3-setuptools \  
python3-pip  
  
ENV DEBIAN_FRONTEND=teletype  
  
WORKDIR /src  
COPY . /src  
  
RUN pip3 install --upgrade pip  
RUN pip3 install -r requirements.pip  
  
EXPOSE 5000  

