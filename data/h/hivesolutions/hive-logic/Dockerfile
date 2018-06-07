FROM hivesolutions/python:latest  
  
LABEL version="1.0"  
LABEL maintainer="Hive Solutions <development@hive.pt>"  
  
EXPOSE 8080  
VOLUME /workers  
VOLUME /data/letsencrypt  
VOLUME /etc/letsencrypt  
VOLUME /var/lib/letsencrypt  
  
ENV LEVEL INFO  
ENV HOST 0.0.0.0  
ENV PORT 8080  
ENV SAFE 0  
ENV CHILDREN 0  
ADD proxy.py /proxy.py  
  
RUN pip3 install --upgrade "netius<1.17.0" hpack appier  
  
CMD ["/usr/bin/python3", "/proxy.py"]  

