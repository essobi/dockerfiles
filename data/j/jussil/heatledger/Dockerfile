FROM openjdk:8  
MAINTAINER Jussi Lindfors  
LABEL version="2.4.0"  
  
ENV SERVER_ROOT=/server  
ENV SERVER_BIN="${SERVER_ROOT}/bin/heatledger"  
ENV SERVER_VERSION="2.4.0"  
ENV SERVER_VERSION_ZIP="heatledger-${SERVER_VERSION}"  
ENV SERVER_PROPERTY_PREFIX="heat__"  
ENV SERVER_PROPERTY_FILE="heat.properties"  
RUN apt-get update \  
&& apt-get install -yy curl screen \  
&& rm -Rf /var/lib/apt/lists/* \  
&& rm -Rf /usr/share/doc && rm -Rf /usr/share/man \  
&& apt-get clean  
  
RUN cd /tmp \  
&& wget -q -P /tmp https://github.com/Heat-Ledger-
Ltd/heatledger/releases/download/v${SERVER_VERSION}/${SERVER_VERSION_ZIP}.zip
\  
&& unzip ${SERVER_VERSION_ZIP}.zip \  
&& mv ${SERVER_VERSION_ZIP} ${SERVER_ROOT} \  
&& rm -rf /tmp/*  
  
ADD *.sh /  
RUN chmod +x /*.sh  
  
EXPOSE 7733 7734 7744 7755  
CMD ["/run.sh"]  

