FROM debian:jessie  
MAINTAINER Philipp Holler <philipp.holler93@googlemail.com>  
  
ENV ETHERPAD_VERSION="1.5.7" \  
ETHERPAD_INSTALLDIR="/opt/etherpad-lite" \  
ETHERPAD_DATADIR="/var/lib/etherpad-lite"  
RUN useradd -r -m etherpad-lite  
  
RUN apt-get update \  
&& apt-get install -y gzip git curl python libssl-dev pkg-config build-
essential nodejs npm mysql-client \  
&& rm -r /var/lib/apt/lists/*  
  
RUN mkdir ${ETHERPAD_INSTALLDIR} \  
&& git clone \--branch ${ETHERPAD_VERSION} git://github.com/ether/etherpad-
lite.git ${ETHERPAD_INSTALLDIR} \  
&& ln -s /usr/bin/nodejs /usr/bin/node  
  
VOLUME ${ETHERPAD_DATADIR}  
  
EXPOSE 9001  
ADD /etherpad-lite_entrypoint.sh /  
RUN chmod +x /etherpad-lite_entrypoint.sh  
ENTRYPOINT ["/etherpad-lite_entrypoint.sh"]  

