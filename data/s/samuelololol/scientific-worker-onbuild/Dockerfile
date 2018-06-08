FROM selenium/standalone-chrome  
MAINTAINER samuelololol<samuelololol@gmail.com>  
USER root  
ONBUILD RUN mkdir -p /app  
ONBUILD WORKDIR /app  
ONBUILD COPY . /app  
ONBUILD RUN pip install -r requirements.txt  
RUN apt-get update &&\  
apt-get install -y python-sklearn python-dev python-pip python-pyaudio sox \  
portaudio19-dev libatlas-base-dev postgresql postgresql-contrib libpq-dev &&\  
pip install --upgrade pip &&\  
pip install pyaudio gevent matplotlib numpy scipy requests pytest bottle \  
BeautifulSoup celery[redis] &&\  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt-lists/*  

