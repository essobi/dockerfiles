FROM openjdk:8-alpine  
  
# Disable warnings  
ENV LEIN_ROOT=1  
  
RUN apk add --update wget ca-certificates bash tzdata && \  
wget -q
"https://raw.githubusercontent.com/technomancy/leiningen/2.6.1/bin/lein" -O
/usr/local/bin/lein && \  
chmod 0755 /usr/local/bin/lein && \  
lein --version && \  
# Set timezone  
export TZ=Europe/Vienna && \  
cp /usr/share/zoneinfo/$TZ /etc/localtime && \  
echo $TZ > /etc/timezone && \  
# Cleanup  
apk del wget tzdata && \  
rm -rf /tmp/* /var/cache/apk/*  

