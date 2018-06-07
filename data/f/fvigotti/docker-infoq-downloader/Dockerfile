FROM ubuntu:14.04  
RUN apt-get update && \  
apt-get -y --quiet upgrade && \  
apt-get -y --quiet install libxml2-dev libxslt1-dev git python python-
setuptools python-dev build-essential libz-dev && \  
easy_install pip && \  
apt-get -y clean  
  
WORKDIR /opt  
  
RUN git clone https://github.com/berdario/infoq-downloader  
  
WORKDIR /opt/infoq-downloader  
  
RUN pip install -r requirements.txt  
  
RUN mkdir /opt/infoq-downloader/downloads  
  
VOLUME /opt/infoq-downloader/downloads  
  
WORKDIR /opt/infoq-downloader  
ENTRYPOINT ["python", "infoq_downloader.py"]  

