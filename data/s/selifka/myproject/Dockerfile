FROM ubuntu:xenial  
WORKDIR /src  
COPY . /src  
  
RUN apt-get update && apt-get install -y \  
apt-utils \  
build-essential \  
python3 \  
python3-dev \  
python3-setuptools \  
python3-pip  
  
RUN pip3 install --upgrade pip  
RUN pip3 install Flask==0.12  
  
# Please note, this EXPOSE command does not publish port 8080  
# This has been added so anyone trying to run the container  
# will know what port to map  
EXPOSE 8080  

