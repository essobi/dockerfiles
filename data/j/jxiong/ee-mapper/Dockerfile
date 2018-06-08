# x86 architecture  
FROM debian:jessie  
  
MAINTAINER Jun Xiong "jun.xiong1981@gmail.com"  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-utils \  
python \  
build-essential \  
make \  
gcc \  
g++ \  
python-dev \  
python-flask \  
python-gdal \  
libffi-dev \  
python-pip  
  
EXPOSE 5000  
# server  
RUN pip install --upgrade pip  
RUN pip install google-api-python-client  
RUN pip install pyCrypto  
RUN apt-get install -y libssl-dev  
RUN pip install earthengine-api  
ADD Crypto /home/Crypto  
ADD ee /home/ee  
ADD httplib2 /home/httplib2  
ADD oauth2client /home/oauth2client  
ADD static /home/static  
ADD templates /home/templates  
COPY app.py /home/app.py  
RUN chmod +x /home/app.py  
  
WORKDIR /home  
CMD /bin/bash  

