FROM debian:jessie-backports  
MAINTAINER WOW! Group Development  
  
ADD deb /tmp/  
  
RUN apt-get -y update \  
&& apt-get -y dist-upgrade \  
&& apt-get -y -t jessie-backports install collectd \  
&& dpkg -i /tmp/collectd-core_*.deb /tmp/collectd_*.deb \  
&& apt-get -y install python-pip python-six \  
&& pip install boto3 \  
&& apt-get -y purge --auto-remove python-pip \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD collectd.conf /etc/collectd/  
ADD write_cloudwatch.py /usr/local/lib/collectd/python/  
  
EXPOSE 8125/udp  
ENTRYPOINT ["/usr/sbin/collectd", "-f"]  

