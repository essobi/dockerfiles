FROM alpine:latest  
  
COPY murmur.ini /tmp/murmur.ini  
COPY start.sh /start  
  
# init some stuff  
# also get the latest mumble version from github api  
RUN apk --no-cache add \  
openssl \  
pwgen \  
jq \  
curl \  
&& addgroup -g 1000 murmur \  
&& adduser -DS -s /bin/false -u 1000 -G murmur murmur \  
&& mkdir -p \  
/opt/murmur/ \  
/opt/db/ \  
/var/log/murmur \  
/var/run/murmur \  
&& MURMUR_LATEST=$(curl https://api.github.com/repos/mumble-
voip/mumble/releases/latest | jq -r .tag_name) \  
&& wget https://github.com/mumble-
voip/mumble/releases/download/${MURMUR_LATEST}/murmur-
static_x86-${MURMUR_LATEST}.tar.bz2 -O - |\  
bzcat -f |\  
tar -x -C /opt -f - \  
&& mv -f /opt/murmur-*/* /opt/murmur/ \  
&& chmod 700 /start  
  
  
EXPOSE 64738/udp 64738/tcp  
  
VOLUME ["/etc/murmur", "/opt/db/", "/var/log/murmur"]  
  
ENTRYPOINT [ "/start" ]  
  
ENV UID=1000 GID=1000 \  
DATABASE=/opt/db/murmur.sqlite \  
DB_DRIVER= \  
DB_USERNAME= \  
DB_PASSWORD= \  
DB_HOST= \  
DB_PORT=3306 \  
DB_PREFIX=murmur_ \  
DB_OPTS="UNIX_SOCKET=/opt/db/mysqld.sock" \  
HOST=0.0.0.0 \  
USER_COUNT=50 \  
SERVER_PASSWORD= \  
WELCOME_TEXT="Welcome to this server running murmur-docker !" \  
SERVER_NAME=  
  

