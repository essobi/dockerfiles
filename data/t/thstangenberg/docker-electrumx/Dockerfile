FROM python:3  
MAINTAINER Thorben Stangenberg <thorben@stangenberg.net>  
  
ARG ELECTRUMX_VERSION=1.0.10  
RUN apt-get update && \  
apt-get install libleveldb-dev -y && \  
pip install git+git://github.com/kyuupichan/electrumx.git@${ELECTRUMX_VERSION}
&& \  
useradd electrumx && \  
mkdir /srv/db && \  
chown electrumx:electrumx /srv/db  
  
ENV DB_DIRECTORY=/srv/db  
ENV DAEMON_URL=electrumx:electrumx@bitcoind  
ENV HOST=  
ENV TCP_PORT=50001  
ENV SSL_PORT=50002  
ENV SSL_CERTFILE=/srv/db/server.crt  
ENV SSL_KEYFILE=/srv/db/server.key  
  
ENV DONATION_ADDRESS=1A2ZyT1QcbGf9FGv4skRi7ynDxsGuE7Rpz  
  
COPY motd /srv/motd  
  
ENV BANNER_FILE=/srv/motd  
  
USER electrumx  
  
VOLUME /srv/db  
EXPOSE 50001  
EXPOSE 50002  
ENTRYPOINT ["electrumx_server.py"]  

