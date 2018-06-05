FROM wordpress:4.8  
MAINTAINER Maik Hummel <m@ikhummel.com>  
  
ENV WORDPRESS_PLUGINS="hello-dolly" \  
SITE_URL=https://beevelop.com \  
SITE_TITLE="DockerPress" \  
ADMIN_USER=docker \  
ADMIN_EMAIL="changeme@example.com" \  
ADMIN_PASSWORD=Un1c0rn \  
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

