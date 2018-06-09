FROM python:3  
#FROM python:3-alpine  
MAINTAINER Tornike Zedginidze <tokozedg@gmail.com>  
  
#required by sphinx-spelling  
RUN \  
apt-get update && apt-get install -y --no-install-recommends \  
python-enchant \  
make && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#RUN apk add --update enchant-dev && rm /var/cache/apk/*  
RUN \  
pip install sphinx sphinxcontrib-spelling sphinxcontrib-programoutput \  
sphinxcontrib-seqdiag sphinxcontrib-actdiag sphinxcontrib-blockdiag \  
sphinxcontrib-nwdiag sphinx-autobuild  
  
COPY . /sphinx/  
CMD make livehtml  
WORKDIR /sphinx/  
  
EXPOSE 8000  

