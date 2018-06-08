FROM alpine:3.4  
RUN apk add --no-cache ca-certificates  
  
ENV LETSENCRYPT_RELEASE 0.0.1  
ADD https://github.com/asosgaming/asos-
letsencrypt/releases/download/${LETSENCRYPT_RELEASE}/asos-letsencrypt-linux-
amd64.tar.gz /tmp/asos-letsencrypt.tar.gz  
  
RUN tar -zxvf /tmp/asos-letsencrypt.tar.gz -C /usr/bin \  
&& chmod +x /usr/bin/asos-letsencrypt  
  
ENTRYPOINT ["/usr/bin/asos-letsencrypt"]  
EXPOSE 80  

