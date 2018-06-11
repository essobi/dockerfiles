FROM python:2-slim  
  
MAINTAINER Wayne San <waynesan@zerozone.tw>  
  
RUN apt-get update \  
&& apt-get install -y python-twisted  
  
# Clean Up  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN openssl req -x509 -nodes -newkey rsa:2048 \  
-keyout /tmp/server.pem -out /tmp/server.pem \  
-days 365 -subj '/CN=localhost'  
  
EXPOSE 4443  
VOLUME ["/web"]  
  
WORKDIR /tmp  
ENTRYPOINT ["twistd", "-no", "web"]  
CMD ["-p0", "--https", "4443", "-c", "/tmp/server.pem", "-k",
"/tmp/server.pem", "--path", "/web"]  

