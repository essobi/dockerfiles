# confd and supervisord on Ubuntu Trusty  
FROM markusma/supervisord:ubuntu-trusty  
MAINTAINER Markus Mattinen <markus@gamma.fi>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends golang git \  
&& cd /tmp \  
&& git clone https://github.com/kelseyhightower/confd -b v0.10.0 \  
&& cd confd \  
&& cd src/github.com/kelseyhightower/confd \  
&& GOPATH=/tmp/confd:/tmp/confd/vendor: go build . \  
&& mv confd /usr/local/bin/confd \  
&& chmod +x /usr/local/bin/confd \  
&& cd / \  
&& rm -r /tmp/confd \  
&& apt-get purge -y golang git \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD config/etc/confd /etc/confd  
ADD config/init /init  
  
CMD ["/init"]  

