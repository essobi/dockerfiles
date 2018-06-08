FROM ubuntu:vivid  
  
MAINTAINER Kurt Huwig  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
ganglia-monitor \  
ganglia-webfrontend \  
gmetad \  
supervisor \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
RUN ln -s /etc/ganglia-webfrontend/apache.conf /etc/apache2/conf-
available/ganglia.conf \  
&& a2enconf ganglia  
  
COPY files/ /  
  
VOLUME ["/var/lib/ganglia"]  
  
CMD ["/entrypoint.sh"]  
  
EXPOSE 80 8649 8649/udp  

