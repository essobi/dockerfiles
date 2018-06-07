FROM graylog2/server:latest  
  
RUN mkdir -p /usr/share/GeoIP && \  
wget -P /usr/share/GeoIP
http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz && \  
gunzip /usr/share/GeoIP/GeoLite2-City.mmdb.gz  
  
ENV PL_SSO 2.4.2  
ENV PL_SLACK 3.1.0  
  
RUN wget -O /usr/share/graylog/plugin/graylog-plugin-auth-sso.jar
https://github.com/Graylog2/graylog-plugin-auth-
sso/releases/download/$PL_SSO/graylog-plugin-auth-sso-$PL_SSO.jar  
RUN wget -O /usr/share/graylog/plugin/graylog-plugin-slack.jar
https://github.com/graylog-labs/graylog-plugin-
slack/releases/download/$PL_SLACK/graylog-plugin-slack-$PL_SLACK.jar  

