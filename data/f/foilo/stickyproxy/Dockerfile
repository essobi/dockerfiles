FROM ubuntu:13.10  
RUN echo "deb http://de.archive.ubuntu.com/ubuntu/ saucy main main universe" >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y software-properties-common python python-pip mitmproxy  
  
RUN cp /usr/share/doc/mitmproxy/examples/stickycookies /usr/bin/sticky-proxy  
  
RUN chmod +x /usr/bin/sticky-proxy  
  
EXPOSE 8080  
ENTRYPOINT ["sticky-proxy"]  

