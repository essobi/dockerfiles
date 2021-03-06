FROM node:8-stretch  
  
RUN set -ex; \  
if ! command -v gpg > /dev/null; then \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
gnupg \  
dirmngr \  
; \  
rm -rf /var/lib/apt/lists/*; \  
fi  
  
# Install dependencies  
RUN apt-get update \  
&& apt-get -y install ffmpeg \  
&& rm /var/lib/apt/lists/* -fR  
  
# Add peertube user  
RUN groupadd -r peertube \  
&& useradd -r -g peertube -m peertube  
  
# grab gosu for easy step-down from root  
# https://github.com/tianon/gosu/releases  
ENV GOSU_VERSION 1.10  
RUN set -ex; \  
\  
fetchDeps='ca-certificates wget'; \  
apt-get update; \  
apt-get install -y --no-install-recommends $fetchDeps; \  
rm -rf /var/lib/apt/lists/*; \  
\  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \  
wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch";
\  
wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc";
\  
export GNUPGHOME="$(mktemp -d)"; \  
for server in $(shuf -e ha.pool.sks-keyservers.net \  
hkp://p80.pool.sks-keyservers.net:80 \  
keyserver.ubuntu.com \  
hkp://keyserver.ubuntu.com:80 \  
pgp.mit.edu) ; do \  
gpg --keyserver "$server" \--recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 && break || : ; \  
done; \  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \  
rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc; \  
chmod +x /usr/local/bin/gosu; \  
gosu nobody true; \  
\  
apt-get purge -y --auto-remove wget  
  
# Install PeerTube  
WORKDIR /app  
COPY . ./  
RUN chown -R peertube:peertube /app  
  
USER peertube  
  
RUN yarn install --pure-lockfile \  
&& npm run build  
  
USER root  
  
RUN mkdir /data /config  
RUN chown -R peertube:peertube /data /config  
  
ENV NODE_ENV production  
ENV NODE_CONFIG_DIR /config  
  
VOLUME /data  
VOLUME /config  
  
COPY ./support/docker/production/docker-entrypoint.sh /usr/local/bin/docker-
entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
  
# Run the application  
CMD ["npm", "start"]  
EXPOSE 9000  

