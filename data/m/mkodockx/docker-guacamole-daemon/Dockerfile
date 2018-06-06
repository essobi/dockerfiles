FROM debian:latest  
MAINTAINER https://m-ko-x.de Markus Kosmal <code@m-ko-x.de>  
  
# define env vars  
ENV GUACAMOLE_VERSION 0.9.4  
# get dependencies  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get install -y curl && \  
apt-get install -y gcc make && \  
apt-get install -y libcairo2-dev libpng12-dev libossp-uuid-dev libvncserver-
dev libfreerdp-dev libssl-dev && \  
apt-get install -y libpango1.0-dev libssh2-1-dev libtelnet-dev libpulse-dev
libvorbis-dev  
  
# fetch src  
RUN curl -L -o guacamole-server.tar.gz
http://sourceforge.net/projects/guacamole/files/current/source/guacamole-
server-${GUACAMOLE_VERSION}.tar.gz/download && \  
tar xzf guacamole-server.tar.gz && \  
rm guacamole-server.tar.gz*  
  
# build from src  
RUN cd guacamole-server-${GUACAMOLE_VERSION} && \  
./configure && \  
make install && \  
ldconfig  
  
# clean dev tooling  
RUN apt-get purge -y gcc make && \  
apt-get autoremove -yq && \  
apt-get clean  
  
ENV GUACAMOLE_HOME /guacd  
RUN mkdir -p /guacd  
  
WORKDIR /guacd  
EXPOSE 4822  
CMD ["guacd", "-f", "-b", "0.0.0.0", "-l", "4822"]

