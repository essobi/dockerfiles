FROM alpine:3.5  
MAINTAINER Matt Bentley <mbentley@mbentley.net>  
  
ENV NOTARY_VER=0.4.3  
RUN apk --no-cache add bash curl expect &&\  
curl -ssL
"https://github.com/docker/notary/releases/download/v${NOTARY_VER}/notary-
Linux-amd64" > /usr/local/bin/notary &&\  
chmod +x /usr/local/bin/notary  
  
RUN mkdir /data  
WORKDIR /data  
  
COPY notary_easy_button.sh /notary_easy_button.sh  
  
ENTRYPOINT ["/notary_easy_button.sh"]  

