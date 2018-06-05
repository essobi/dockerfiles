FROM debian:jessie  
MAINTAINER Pavel Belyaev  
  
# Install wget  
RUN apt-get update && apt-get install -y wget  
  
# Add acestream repository  
RUN echo 'deb http://repo.acestream.org/ubuntu/ trusty main' | \  
tee /etc/apt/sources.list.d/acestream.list  
  
# Add acestream key  
RUN wget -q -O - http://repo.acestream.org/keys/acestream.public.key | \  
apt-key add -  
  
# Install software  
RUN apt-get update && apt-get install -y \  
acestream-engine \  
python-gevent \  
python-psutil \  
git \  
supervisor  
  
# Install software  
RUN cd /opt/ && git clone https://github.com/ValdikSS/aceproxy.git aceproxy  
  
# Configuration  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY aceconfig.py /opt/aceproxy/aceconfig.py  
  
# CMD and PORTS  
CMD ["/usr/bin/supervisord"]  
EXPOSE 8000

