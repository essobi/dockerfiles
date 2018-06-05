FROM mono:4.8.0.524  
MAINTAINER mezz64  
  
RUN apt-get update && \  
apt-get install -yq \  
mono-4.0-service \  
supervisor && \  
  
# cleanup  
apt-get clean && \  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
RUN mkdir -p /var/log/supervisor  
  
ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# ports and volumes  
EXPOSE 44456 44454  
VOLUME /config  
  
WORKDIR /config  
  
CMD ["/usr/bin/supervisord"]  

