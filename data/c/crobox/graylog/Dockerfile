FROM graylog2/server:2.4.4-1  
RUN wget -O /usr/share/graylog/plugin/graylog-plugin-auth-sso-2.4.2.jar
https://github.com/Graylog2/graylog-plugin-auth-
sso/releases/download/2.4.2/graylog-plugin-auth-sso-2.4.2.jar  
RUN mkdir -p /opt/geolite && wget -qO-
http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz | tar
xvz --strip-components=1 -C /opt/geolite  
# ADD log4j.xml /etc/graylog/server/log4j.xml  

