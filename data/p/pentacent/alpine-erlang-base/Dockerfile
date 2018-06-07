FROM alpine:3.6  
  
ENV REFRESHED_AT=2017-10-30  
ENV HOME=/opt/app  
ENV TERM=xterm  
  
#Install Dependencies for Erlang  
RUN apk add \--no-cache \  
ncurses-libs \  
zlib \  
openssl \  
ca-certificates && \  
update-ca-certificates --fresh  
  
#Install bash which is required by Distillery  
RUN apk add \--no-cache bash  
  
#Create /opt/app directory and default user  
RUN mkdir -p ${HOME} && \  
adduser -s /bin/sh -u 1001 -G root -h ${HOME} -S -D default && \  
chown -R 1001:0 ${HOME} && \  
apk --no-cache upgrade  
  
WORKDIR ${HOME}  
CMD ["/bin/sh"]  

