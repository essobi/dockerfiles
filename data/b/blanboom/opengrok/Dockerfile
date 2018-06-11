# Dockerfile for OpenGrok  
FROM tomcat:8.5-jre8  
  
# Name of OpenGrok zip file.  
ENV OPENGROKVERSIONCODE 1.1-rc16  
ENV OPENGROKVERSION opengrok-${OPENGROKVERSIONCODE}  
ENV OPENGROKZIP
https://github.com/OpenGrok/OpenGrok/releases/download/${OPENGROKVERSIONCODE}/${OPENGROKVERSION}.tar.gz  
  
# Environment needed to deploy opengrok  
ENV OPENGROK_APP_SERVER=Tomcat  
ENV OPENGROK_WAR_TARGET_TOMCAT=$CATALINA_HOME/webapps  
ENV OPENGROK_TOMCAT_BASE=$CATALINA_HOME  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
cron \  
exuberant-ctags \  
git \  
sudo \  
&& curl -LO "$OPENGROKZIP" \  
&& tar xaf ${OPENGROKVERSION}.tar.gz \  
&& useradd -m tomcat \  
&& echo "tomcat:builder" | chpasswd \  
&& echo "00 10 * * 1-5 /usr/local/tomcat/${OPENGROKVERSION}/bin/OpenGrok index
/source" >> crontab \  
&& crontab -u tomcat crontab \  
&& echo "tomcat ALL=NOPASSWD: /usr/sbin/service cron start" >>
/etc/sudoers.d/cron \  
&& mkdir /var/opengrok \  
&& chown tomcat /var/opengrok \  
&& chown -R tomcat . \  
&& echo done  
  
COPY run_tests.sh /usr/local/tomcat/  
VOLUME /source  
USER tomcat  
CMD ${OPENGROKVERSION}/bin/OpenGrok deploy \  
&& find webapps -maxdepth 1 -name source* -execdir \  
sh -c 'mv -u $(basename {}) $(echo $(basename {}) | sed
s/source/${OPENGROK_WEBAPP_CONTEXT:-source}/)' \; \  
&& ${OPENGROKVERSION}/bin/OpenGrok index /source \  
&& sudo service cron start \  
&& catalina.sh run  
  

