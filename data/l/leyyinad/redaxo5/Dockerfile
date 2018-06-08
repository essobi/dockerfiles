FROM businesstools/nginx-php:1.8.0  
WORKDIR /var/www/html  
  
ENV REDAXO_VERSION 5.6.0  
ENV REDAXO_MD5 8f4e4d49ca94cab022d4c297e081f389  
  
RUN apt-get update --no-install-recommends && \  
apt-get -yq --force-yes install unzip mariadb-client && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
/var/www/html/index.nginx-debian.html  
  
COPY bin/redaxo.setup.sh /etc/my_init.d/  
COPY etc/nginx.conf /etc/nginx/conf.d/default.conf  
COPY etc/config.yml.php etc/initdb.sql /src/etc/  
  
RUN curl -Ls -o /tmp/redaxo5.zip \  
"https://github.com/redaxo/redaxo/releases/download/${REDAXO_VERSION}/redaxo_${REDAXO_VERSION}.zip"
&& \  
echo "${REDAXO_MD5} /tmp/redaxo5.zip" | md5sum -c && \  
unzip /tmp/redaxo5.zip && \  
rm /tmp/redaxo5.zip  
  
COPY bin/docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  

