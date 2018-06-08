FROM galloplabs/nodejs  
MAINTAINER Jonathon W. Marshall "jonathon@gallop.io"  
ENV STATSD_VERSION master  
  
RUN apk --update add make g++ python curl \  
&& rm -rf /var/cache/apk/* \  
&& mkdir /opt \  
&& curl -sSL https://github.com/etsy/statsd/archive/$STATSD_VERSION.tar.gz |
tar -v -C /opt -xz \  
&& ln -s /opt/statsd-$STATSD_VERSION /opt/statsd \  
&& cd /opt/statsd \  
&& npm install \  
&& apk del make g++ python curl && rm -rf /var/cache/apk/*  
  
ENV PATH $PATH:/opt/statsd/bin  
  
ADD run.sh /opt/statsd/run.sh  
  
EXPOSE 8125/udp  
EXPOSE 8126  
WORKDIR /opt/statsd  
  
CMD ["/opt/statsd/run.sh"]  

