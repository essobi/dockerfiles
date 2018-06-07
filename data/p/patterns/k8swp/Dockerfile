FROM wordpress:apache  
  
COPY . /opt  
  
RUN apt-get update; \  
apt-get install -y git cron mysql-client; \  
apt-get purge -y --auto-remove; \  
rm -rf /var/lib/apt/lists/*; \  
mkdir -p /root/.ssh; \  
cp /opt/*.sh /root; \  
chmod +x /root/*.sh; \  
cp /opt/sshconf-github /root/.ssh/config; \  
ssh-keyscan -H github.com >> /root/.ssh/known_hosts; \  
curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar && chmod +x wp-cli.phar && mv wp-cli.phar /usr/local/bin/wp;  
  
  
  
# The Wordpress base image entrypoint expects a starting work-dir  
# which will be initialized when found to be empty. The Apache  
# image default is normally /var/www/html  
##WORKDIR /var/www/html  

