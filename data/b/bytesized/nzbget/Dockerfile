FROM bytesized/base  
MAINTAINER maran@bytesized-hosting.com  
  
RUN apk add --no-cache wget && wget -O - http://nzbget.net/info/nzbget-
version-linux.json | \  
sed -n "s/^.*stable-download.*: \"\\(.*\\)\".*/\1/p" | \  
wget --no-check-certificate -i - -O nzbget-latest-bin-linux.run && sh nzbget-
latest-bin-linux.run --destdir /app/nzbget  
  
VOLUME /config /data / media  
COPY /static /  
  
EXPOSE 6789  

