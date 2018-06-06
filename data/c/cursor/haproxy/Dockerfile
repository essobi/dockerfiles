FROM cursor/mbase  
MAINTAINER Ryan Pederson <ryan@pederson.ca>  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections \  
&& add-apt-repository -y ppa:vbernat/haproxy-1.8 \  
&& apt-get update -q \  
&& apt-get -y install supervisor haproxy=1.8.\\* \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /config  
RUN mkdir -p /var/log/supervisor  
  
EXPOSE 443  
EXPOSE 80  
VOLUME /config  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY init /init  
  
RUN chmod +x /init  
  
ENTRYPOINT ["/init"]  

