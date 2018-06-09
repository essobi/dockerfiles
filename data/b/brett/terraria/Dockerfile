FROM debian:jessie  
  
# Modified from Dockerfile created by Ryan Sheehan  
# <https://github.com/ryansheehan/terraria/blob/master/Dockerfile>  
# See LICENSE file.  
LABEL maintainer "Brett Vickers <github.com/beevik>"  
  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& groupadd -r terraria --gid=1000 \  
&& adduser --disabled-password --gecos 'terraria' \--uid 1000 --ingroup
terraria terraria \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends ca-certificates wget \  
&& wget -q -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -q -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& apt-get install -y zip mono-complete \  
&& apt-get clean \  
&& favorites_path="/home/terraria/My Games/Terraria" \  
&& mkdir -p "$favorites_path" \  
&& echo "{}" > "$favorites_path/favorites.json" \  
&& chown -R terraria:terraria "/home/terraria/My Games"  
  
ENV TSHOCK_VERSION=4.3.22 \  
TSHOCK_FILE_POSTFIX=""  
ADD
https://github.com/NyxStudios/TShock/releases/download/v$TSHOCK_VERSION/tshock_$TSHOCK_VERSION.zip
/  
RUN set -x \  
&& unzip tshock_$TSHOCK_VERSION.zip -d /tshock \  
&& rm tshock_$TSHOCK_VERSION.zip \  
&& chown -R terraria:terraria /tshock \  
&& chmod 777 /tshock/TerrariaServer.exe \  
&& gosu terraria true  
  
VOLUME ["/world", "/tshock/ServerPlugins"]  
  
WORKDIR /tshock  
  
ENTRYPOINT ["gosu", "terraria", "mono", "--server", "--gc=sgen", "-O=all",
"TerrariaServer.exe", "-configpath", "/world", "-worldpath", "/world",
"-logpath", "/world"]  

