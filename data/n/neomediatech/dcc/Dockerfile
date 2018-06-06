FROM debian:stable-slim  
MAINTAINER Dario B. <https://hub.docker.com/r/neomediatech/dcc/>  
  
ENV DEBIAN_FRONTEND=noninteractive  
ENV TZ=Europe/Rome  
ENV DCC_VERSION=1.3.162  
RUN apt-get -yq update && apt-get -y --no-install-recommends install \  
apt-utils ca-certificates curl gcc libc-dev make  
  
# Download & Compile DCC  
RUN curl https://www.dcc-servers.net/dcc/source/old/dcc-${DCC_VERSION}.tar.Z |
tar xzf - -C /tmp && ls -l /tmp  
RUN cd /tmp/dcc-${DCC_VERSION} && ./configure --disable-dccm && make install  
  
RUN apt-get purge -yq binutils cpp gcc libc6-dev linux-libc-dev make && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/log/*  
  
COPY dcc_conf /var/dcc/dcc_conf  
COPY start.sh /usr/local/bin/start.sh  
  
RUN chmod +x /usr/local/bin/start.sh  
  
ENV USER_UID=1000  
ENV USER_GID=1000  
EXPOSE 10030  
CMD ["/usr/local/bin/start.sh"]  

