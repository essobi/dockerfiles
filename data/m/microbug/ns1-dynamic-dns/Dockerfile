FROM alpine:3.7  
RUN apk add --no-cache python3 git \  
&& pip3 install pyyaml requests ns1-python \  
&& apk del --no-cache git  
  
ADD dynamic-dns.py /dynamic-dns.py  
ADD prepare-crontab.sh /prepare-crontab.sh  
  
# How often to run in minutes  
ENV FREQUENCY=5  
COPY crontab /etc/crontabs/root  
CMD /prepare-crontab.sh && crond -f -d 8  

