FROM node:6.9.0-slim  
  
# Install Gosu for dropping privs:  
ENV GOSU_VERSION 1.10  
COPY gosu-$GOSU_VERSION-amd64.asc /tmp/gosu.asc  
RUN set -x \  
&& curl -Lo /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /tmp/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" \  
&& chmod +x /usr/local/bin/gosu  
  
# Create user to drop to:  
RUN useradd -g daemon -m -d /tmp app \  
&& mkdir /app \  
&& chown app:daemon /app  
  
# Install node dependencies:  
WORKDIR /app  
COPY start.sh /app/  
COPY npm-shrinkwrap.json /app/  
COPY package.json /app/  
RUN gosu app npm install --no-optional  
  
EXPOSE 8080  
ENV PORT 8080  
# Install remainder of code:  
COPY . /app  
  
ENTRYPOINT ["/app/start.sh"]  
  

