# Dockerfile for OpenGrok  
FROM tomcat:8.5-jre8-alpine  
  
# Name of OpenGrok zip file.  
ENV OPENGROKVERSIONCODE 1.0  
ENV OPENGROKVERSION opengrok-${OPENGROKVERSIONCODE}  
ENV OPENGROKZIP
https://github.com/OpenGrok/OpenGrok/releases/download/${OPENGROKVERSIONCODE}/${OPENGROKVERSION}.tar.gz  
  
# Environment needed to deploy opengrok  
ENV OPENGROK_APP_SERVER=Tomcat  
ENV OPENGROK_WAR_TARGET_TOMCAT=$CATALINA_HOME/webapps  
ENV OPENGROK_TOMCAT_BASE=$CATALINA_HOME  
  
RUN apk update \  
&& apk add \  
ctags \  
curl \  
dcron \  
git \  
sudo \  
&& curl -LO "${OPENGROKZIP}" \  
&& tar xzf ${OPENGROKVERSION}.tar.gz \  
&& adduser -D tomcat \  
&& echo "tomcat:builder" | chpasswd \  
&& echo "00 10 * * 1-5 /usr/local/tomcat/${OPENGROKVERSION}/bin/OpenGrok index
/data" >> crontab \  
&& crontab -u tomcat crontab \  
&& echo "tomcat ALL=NOPASSWD: /usr/sbin/crond" >> /etc/sudoers.d/cron \  
&& mkdir /var/opengrok \  
&& chown tomcat /var/opengrok \  
&& chown -R tomcat . \  
&& echo done  
  
COPY run_tests.sh /usr/local/tomcat/  
VOLUME /data  
USER tomcat  
CMD ${OPENGROKVERSION}/bin/OpenGrok deploy \  
&& find webapps -maxdepth 1 -name source* -exec \  
sh -c 'mv -n {} $(dirname {})/$(echo $(basename {}) | sed
s/source/${OPENGROK_WEBAPP_CONTEXT:-source}/)' \; \  
&& ${OPENGROKVERSION}/bin/OpenGrok index /data \  
&& sudo crond \  
&& catalina.sh run  
  

