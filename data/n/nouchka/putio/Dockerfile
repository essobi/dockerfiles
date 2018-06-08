FROM debian:jessie  
MAINTAINER Jean-Avit Promis "docker@katagena.com"  
LABEL org.label-schema.vcs-url="https://github.com/nouchka/docker-putio"  
LABEL version="2.0"  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install php5-cli php5-curl git
rsync && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /root  
  
RUN git clone https://github.com/nicoSWD/put.io-api-v2.git && \  
mv put.io-api-v2/src/PutIO/ . && \  
sed -i "s|\\\\\true|\\\\\false|" /root/PutIO/Helpers/PutIO/PutIOHelper.php  
  
RUN mkdir -p download/  
COPY Putio.php /root/Putio.php  
COPY start.sh /start.sh  
RUN chmod +x /start.sh  
  
volume ["/root/download/"]  
  
CMD ["/bin/bash", "-e", "/start.sh"]  

