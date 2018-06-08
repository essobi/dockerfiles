FROM debian:stretch  
RUN apt-get update -qy \  
&& apt-get install --no-install-recommends -qfy python3 python3-dev
python3-pip \  
python3-setuptools python3-wheel build-essential \  
&& apt-get clean \  
&& pip3 install pyinstaller==3.3.1  
  

