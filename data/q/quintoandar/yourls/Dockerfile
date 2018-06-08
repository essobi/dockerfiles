FROM fbcbarbosa/yourls:1.0  
MAINTAINER Fernando Barbosa <fernando.barbosa@quintoandar.com.br>  
  
# Install New Relic  
ENV NR_INSTALL_SILENT true  
ENV NR_APP_NAME yourls  
ENV PLUGIN_DIR /var/www/html/user/plugins  
RUN mkdir -p /opt/newrelic  
WORKDIR /opt/newrelic  
RUN apt-get update && apt-get -yqq install \  
python-setuptools \  
unzip \  
wget && \  
easy_install pip && \  
wget -r -nd --no-parent -Alinux.tar.gz \  
http://download.newrelic.com/php_agent/release/ >/dev/null 2>&1 \  
&& tar -xzf newrelic-php*.tar.gz --strip=1 && \  
bash newrelic-install install && \  
pip install newrelic-plugin-agent && \  
mkdir -p /var/log/newrelic && \  
mkdir -p /var/run/newrelic && \  
curl
https://raw.githubusercontent.com/llonchj/yourls_plugins/master/qs_forward/plugin.php
\  
\--create-dirs -o $PLUGIN_DIR/qs-fordward/plugin.php && \  
curl https://raw.githubusercontent.com/claytondaley/yourls-api-
delete/master/plugin.php \  
\--create-dirs -o $PLUGIN_DIR/yourls-api-delete/plugin.php && \  
curl https://raw.githubusercontent.com/YOURLS/force-
lowercase/master/plugin.php \  
\--create-dirs -o $PLUGIN_DIR/force-lowercase/plugin.php && \  
curl
https://raw.githubusercontent.com/timcrockford/302-instead/master/plugin.php \  
\--create-dirs -o $PLUGIN_DIR/302-instead/plugin.php && \  
wget https://diegopeinador.com/fallback-url.zip && \  
unzip fallback-url.zip -d $PLUGIN_DIR -x '__MACOSX/*' && \  
rm fallback-url.zip && \  
chmod +x -R $PLUGIN_DIR && \  
apt-get purge -y \  
python-setuptools \  
unzip \  
wget && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /var/www/html  
COPY docker-entrypoint.sh .  
ENTRYPOINT ["./docker-entrypoint.sh"]  

