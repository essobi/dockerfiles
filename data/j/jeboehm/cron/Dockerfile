FROM alpine:latest  
  
ENV TZ=Europe/Berlin  
RUN apk --no-cache add \  
docker \  
supervisor \  
tzdata \  
wget && \  
ln -sf /usr/share/zoneinfo/$TZ /etc/localtime && \  
wget https://github.com/jwilder/docker-gen/releases/download/0.7.3/docker-gen-
linux-amd64-0.7.3.tar.gz && \  
tar xvzf docker-gen-linux-amd64-0.7.3.tar.gz && \  
mv docker-gen /usr/bin/ && \  
rm -f docker-gen-linux-amd64-0.7.3.tar.gz && \  
apk --no-cache del \  
wget  
  
COPY crontab.tmpl /etc/crontab.tmpl  
COPY supervisord.conf /etc/supervisord.conf  
  
VOLUME ["/etc/crontabs"]  
CMD ["supervisord", "-c", "/etc/supervisord.conf"]  

