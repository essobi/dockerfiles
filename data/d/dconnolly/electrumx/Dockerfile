FROM python:3  
ARG ELECTRUMX_VERSION=1.2.1  
RUN apt-get update && \  
apt-get install libleveldb-dev -y && \  
pip install git+git://github.com/kyuupichan/electrumx.git@${ELECTRUMX_VERSION}
&& \  
useradd electrumx && \  
mkdir /srv/db && \  
chown electrumx:electrumx /srv/db  
  
ENV COIN=BitcoinCash  
ENV DB_DIRECTORY=/srv/db  
ENV DAEMON_URL=electrumx:electrumx@bitcoind  
ENV HOST=  
ENV TCP_PORT=50001  
ENV SSL_PORT=50002  
ENV SSL_CERTFILE=/srv/server.crt  
ENV SSL_KEYFILE=/srv/server.key  
  
ENV DONATION_ADDRESS=none  
  
COPY motd /srv/motd  
  
ENV BANNER_FILE=/srv/motd  
  
USER electrumx  
  
VOLUME /srv/db  
EXPOSE 50001  
EXPOSE 50002  
ENTRYPOINT ["electrumx_server.py"]  

