FROM ubuntu:14.04.3  
MAINTAINER Dmitry Mozzherin  
ENV LAST_FULL_REBUILD 2016-02-25  
RUN apt-get update && apt-get upgrade -y && \  
apt-get -y install build-essential git-core python \  
python-setuptools python-dev python-numpy python-sklearn \  
python-tornado python-pip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pip install nltk  
RUN python -c "import nltk; nltk.download('punkt')"  
  
RUN git clone https://github.com/mbl-cli/NetiNeti.git app && \  
rm -rf /app/.git  
RUN cp /app/config/neti_http_config.cfg.example
/app/config/neti_http_config.cfg  
  
WORKDIR /app  
  
CMD ["python", "neti_tornado_server.py"]  

