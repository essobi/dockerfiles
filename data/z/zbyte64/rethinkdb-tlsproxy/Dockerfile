FROM rethinkdb:latest  
  
MAINTAINER Jason Kraus <jkraus@editllc.com>  
  
ENV RETHINKDB_JOIN_ADDR 127.0.0.1:29105  
RUN mkdir -p /certs  
RUN mkdir -p /opt  
  
RUN apt-get update \  
&& apt-get install -y stunnel4 \  
&& rm -rf /var/lib/apt/lists/*  
  
#TLS certs go here  
VOLUME ["/certs"]  
  
COPY resources /opt  
RUN chmod +x /opt/run.sh  
  
EXPOSE 28443  
CMD ["/opt/run.sh"]  

