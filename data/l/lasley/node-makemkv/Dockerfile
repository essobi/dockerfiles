FROM lasley/makemkvcon:latest  
MAINTAINER Dave Lasley <dave@dlasley.net>  
  
ENV DIR_OUT='/var/done' \  
DIR_SRC='/var/src' \  
CONVERSION_PROFILE='/opt/node-makemkv/conversion_profile.xml' \  
HTTP_PORT='80' \  
OUTLIER_MODIFIER='0.7' \  
APP_KEY=''  
  
# Install dependencies.  
RUN buildDeps=' \  
build-essential \  
git \  
gnupg2 \  
libudev-dev \  
lsb-release \  
wget \  
'; \  
\  
apt-get update; \  
apt-get install -y --no-install-recommends $buildDeps; \  
wget --no-check-certificate -O nodesource_setup.sh
https://deb.nodesource.com/setup_6.x; \  
\  
bash nodesource_setup.sh; \  
rm nodesource_setup.sh; \  
apt-get install -y nodejs; \  
\  
npm update -g npm; \  
npm install -g coffee-script; \  
\  
git clone https://github.com/lasley/node-makemkv.git /opt/node-makemkv; \  
\  
cd /opt/node-makemkv || exit; \  
npm install ./; \  
\  
mv /opt/node-makemkv/settings.example.json /opt/node-makemkv/settings.json; \  
mv /opt/node-makemkv/conversion_profile.example.xml /opt/node-
makemkv/conversion_profile.xml; \  
\  
rm -rf /var/lib/apt/lists/*; \  
apt-get purge -y --auto-remove $buildDeps;  
  
COPY entrypoint.d/ /entrypoint.d/  
  
WORKDIR /opt/node-makemkv  
  
VOLUME ["/var/done"]  
EXPOSE 80  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/bin/coffee", "/opt/node-makemkv/server.coffee"]  

