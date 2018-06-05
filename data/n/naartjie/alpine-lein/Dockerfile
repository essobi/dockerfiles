FROM frolvlad/alpine-oraclejdk8:slim  
# FROM anapsix/alpine-java  
# install leiningen  
ENV LEIN_ROOT 1  
RUN apk add --update wget ca-certificates bash && \  
wget -q
"https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein" \  
-O /usr/local/bin/lein && \  
chmod 0755 /usr/local/bin/lein && \  
lein && \  
apk del wget ca-certificates && \  
rm -rf /tmp/* /var/cache/apk/*  
  
# install git (for version tagging)  
RUN apk add --no-cache git && \  
rm -rf /tmp/* /var/cache/apk/*  

