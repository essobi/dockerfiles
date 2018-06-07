FROM hivesolutions/pypy:latest  
  
LABEL version="1.0"  
LABEL maintainer="Hive Solutions <development@hive.pt>"  
  
EXPOSE 1080  
VOLUME /data  
  
ENV LEVEL INFO  
ENV HOST 0.0.0.0  
ENV PORT 1080  
RUN pip install --upgrade netius  
  
CMD ["/usr/bin/python", "-m", "netius.servers.socks"]  

