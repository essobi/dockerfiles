# supervisord on Ubuntu Trusty  
FROM markusma/ubuntu:trusty  
MAINTAINER Markus Mattinen <markus@gamma.fi>  
  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends python-setuptools \  
&& git clone https://github.com/MarkusMattinen/supervisor.git -b prepend-
timestamp /tmp/supervisor \  
&& cd /tmp/supervisor \  
&& easy_install . \  
&& ln -sf /usr/local/bin/supervisord /usr/bin/supervisord \  
&& ln -sf /usr/local/bin/pidproxy /usr/bin/pidproxy \  
&& cd / \  
&& rm -rf /tmp/supervisor \  
&& apt-get purge -y python-setuptools \  
&& apt-get install -y \--no-install-recommends python-pkg-resources \  
&& apt-get autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& mkdir -p /var/log/supervisor  
  
ADD config/etc/supervisor/supervisord.conf /etc/supervisor/supervisord.conf  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

