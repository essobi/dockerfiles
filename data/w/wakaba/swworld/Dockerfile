FROM wakaba/docker-perl-app-base  
  
RUN apt-get update && \  
DEBIAN_FRONTEND="noninteractive" apt-get -y install mysql-server
libmysqlclient-dev socat && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mv /app /app.orig && \  
git clone https://bitbucket.org/wakabatan/swworld.git /app && \  
mv /app.orig/* /app/ && \  
cd /app && make deps PMBP_OPTIONS=\--execute-system-package-installer && \  
echo '#!/bin/bash' > /server && \  
echo 'export MYSQL_DSNS_JSON=/config/dsns.json' >> /server && \  
echo 'export KARASUMA_CONFIG_FILE_DIR_NAME=/config/keys' >> /server && \  
echo 'export KARASUMA_CONFIG_JSON=/config/config.json' >> /server && \  
echo 'socat tcp-listen:6235,fork unix:/wpserver/wpserver.sock &' >> /server &&
\  
echo 'cd /app && ./plackup bin/server.psgi -p 8080 -s Twiggy::Prefork \--max-
workers 5' >> /server && \  
chmod u+x /server && \  
rm -fr /app/deps /app.orig  

