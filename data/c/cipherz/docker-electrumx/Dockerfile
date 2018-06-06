FROM python:3.6-alpine3.6  
LABEL maintainer="cipherz <dev@cipherz.com>"  
  
COPY ./bin /usr/local/bin  
  
RUN chmod a+x /usr/local/bin/* && \  
apk add --no-cache git build-base openssl && \  
apk add --no-cache --repository http://nl.alpinelinux.org/alpine/edge/testing
leveldb-dev && \  
pip install aiohttp pylru plyvel && \  
git clone https://github.com/cipherzzz/electrumx.git && \  
cd electrumx && \  
python setup.py install && \  
apk del git build-base && \  
rm -rf /tmp/*  
  
VOLUME ["/data"]  
ENV HOME /data  
ENV ALLOW_ROOT 1  
ENV DB_DIRECTORY /data  
ENV TCP_PORT=50001  
ENV SSL_PORT=50002  
ENV SSL_CERTFILE ${DB_DIRECTORY}/electrumx.crt  
ENV SSL_KEYFILE ${DB_DIRECTORY}/electrumx.key  
ENV HOST ""  
WORKDIR /data  
  
EXPOSE 50001 50002  
CMD ["init"]  

