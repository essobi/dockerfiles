FROM debian:8  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq update && apt-get -qq -y --no-install-recommends install \  
ca-certificates \  
curl \  
python \  
python-pip  
  
RUN mkdir /etc/supervisord \  
&& mkdir /etc/supervisord/conf.d \  
&& mkdir /var/log/supervisord \  
&& pip install supervisor  
  
COPY supervisord.conf /etc/supervisord/  
  
CMD ["/usr/local/bin/supervisord", "-c", "/etc/supervisord/supervisord.conf"]  

