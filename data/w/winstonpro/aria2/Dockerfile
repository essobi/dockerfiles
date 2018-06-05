FROM alpine:latest  
ENV VERSION 0.2.0  
RUN apk --update \--no-cache add aria2 nginx libc6-compat ca-certificates wget
openssl unzip && \  
update-ca-certificates && \  
wget https://github.com/mayswind/AriaNg/releases/download/${VERSION}/aria-
ng-${VERSION}.zip -O ariang.zip && \  
mkdir /home/ariang && mv ariang.zip /home/ariang && cd /home/ariang && unzip
ariang.zip && rm ariang.zip && \  
mkdir -p /root/.aria2 && mkdir /run/nginx && \  
apk del wget unzip  
COPY aria2.conf /root/.aria2/aria2.conf  
COPY default.conf /etc/nginx/conf.d/default.conf  
COPY start.sh /start.sh  
COPY hook.sh /hook.sh  
RUN chmod +x *.sh  
EXPOSE 80 6800  
  
CMD ["/start.sh"]  

