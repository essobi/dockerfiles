FROM debian:stable  
MAINTAINER Michael Kaldawi <mkaldawi@gmail.com>  
LABEL Description="This image runs drone simulator software on debian."  
  
RUN apt-get update && apt-get install -y \  
python \  
wget \  
git  
  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
RUN pip install pyowm  
RUN pip install geopy  
RUN pip install simples3  
RUN pip install dweepy  
RUN pip install python-dateutil  
RUN pip install pytz  
  
RUN git clone -b master
https://2372f8e264fd8279b085c69e93286cae18b05ba6:x-oauth-
basic@github.com/VerizonCloud/IoT.git /github  
RUN mv /github/dweet /  
RUN rm -r /github  

