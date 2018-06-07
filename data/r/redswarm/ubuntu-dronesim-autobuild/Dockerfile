FROM ubuntu:14.04  
MAINTAINER Michael Kaldawi <mkaldawi@gmail.com>  
  
LABEL Description="This image runs drone simulator software on Ubuntu 14.04."  
RUN apt-get update && apt-get install -y \  
python \  
wget \  
unzip  
  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
RUN pip install pyowm  
RUN pip install geopy  
RUN pip install simples3  
RUN pip install dweepy  
RUN pip install python-dateutil  
RUN pip install pytz  
  
RUN wget https://github.com/michael-kaldawi/dronesim/archive/master.zip  
RUN unzip master.zip  

