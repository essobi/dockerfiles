FROM alpine:3.5  
ADD nginx.conf /app/  
ADD Procfile /app/  
  
# Download and install rtorrent  
RUN apk --no-cache --no-progress add ca-certificates nginx nodejs bash && \  
apk --no-cache --no-progress --virtual=.build-dependencies add git tar gzip
openssl && \  
update-ca-certificates && \  
cd /usr/local/bin && wget -qO- "https://bin.equinox.io/c/ekMN3bCZFUn/forego-
stable-linux-amd64.tgz" | tar xz && \  
chmod u+x /usr/local/bin/forego && \  
cd /app && git clone https://github.com/jfurrow/flood.git && \  
cd /app/flood && npm install --production && \  
apk --no-progress del .build-dependencies && \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log && \  
mkdir -p /data/db  
  
ADD config.js /app/flood/  
  
EXPOSE 80  
VOLUME [/data/db]  
  
WORKDIR /app  
  
CMD ["forego", "start"]  

