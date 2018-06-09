FROM ubuntu:trusty  
WORKDIR /usr/src/app  
RUN set -ex && \  
apt-get update && \  
apt-get install -y supervisor ca-certificates python git rsyslog --no-install-
recommends && \  
apt-get clean && \  
git clone https://github.com/modoboa/modoboa-installer.git /usr/src/app/ && \  
./run.py --force localhost  
COPY files /  
CMD ["supervisord"]  

