FROM hivesolutions/pypy:latest  
  
LABEL version="1.0"  
LABEL maintainer="Hive Solutions <development@hive.pt>"  
  
EXPOSE 8080  
VOLUME /data  
  
ENV LEVEL INFO  
ENV HOST 0.0.0.0  
ENV PORT 8080  
ENV CACHE 86400  
ENV CORS 1  
ENV BASE_PATH /data  
  
RUN pip install --upgrade netius  
  
CMD ["/usr/bin/python", "-m", "netius.extra.filea"]  

