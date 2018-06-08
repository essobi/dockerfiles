FROM alpine  
  
USER root  
COPY wget.py /usr/bin/wget.py  
  
RUN apk update && \  
apk add --no-cache python bash && \  
mv /usr/bin/wget.py /usr/bin/wget && \  
chmod a+x /usr/bin/wget && \  
rm -rf /var/cache/*  
  
ENTRYPOINT ["bash"]  

