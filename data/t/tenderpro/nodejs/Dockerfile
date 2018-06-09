FROM debian:jessie  
  
MAINTAINER Alexey Kovrizhkin <lekovr+tpro@gmail.com>  
  
ENV DOCKERFILE_VERSION 171017  
ENV GOSU_VER=1.10  
RUN apt-get update && apt-get install -y \  
curl sudo \  
&& arch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/${GOSU_VER}/gosu-$arch" \  
&& chmod +x /usr/local/bin/gosu \  
&& curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - \  
&& apt-get install -y nodejs bzip2 libfontconfig1 \  
&& rm -rf /var/lib/apt/lists/*  
  
#
-------------------------------------------------------------------------------  
# user op  
RUN useradd -m -r -s /bin/bash -Gwww-data -gusers -gsudo op  
  
#
-------------------------------------------------------------------------------  
# Extra libs  
COPY package.json /home/op  
RUN cd /home/op \  
&& chown op /usr/lib/node_modules \  
&& ln -s /usr/lib/node_modules node_modules \  
&& npm install --only=dev  
  
#
-------------------------------------------------------------------------------  
# Consup  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
WORKDIR /home/app  
VOLUME /home/app  
  
ENV APPUSER op  

