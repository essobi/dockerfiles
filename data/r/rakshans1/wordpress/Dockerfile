FROM wordpress:4.8  
LABEL MAINTAINER="Rakshan Shetty <shetty.raxx555@gmail.com>"  
  
ENV WORDPRESS_PLUGINS="hello-dolly" \  
SITE_URL=http://rakshanshetty.in \  
SITE_TITLE="DockerPress" \  
ADMIN_USER=admin \  
ADMIN_EMAIL="changeme@example.com" \  
ADMIN_PASSWORD=12345678 \  
WORDPRESS_ACTIVE_THEME=twentysixteen \  
WORDPRESS_THEMES="twentysixteen;twentyfifteen"  
COPY launch /  
  
RUN apt-get -qq update && apt-get -qq install netcat && \  
curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar && \  
chmod +x wp-cli.phar && \  
mv wp-cli.phar /usr/local/bin/wp && \  
chmod +x /launch && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
ENTRYPOINT []  
  
CMD /launch

