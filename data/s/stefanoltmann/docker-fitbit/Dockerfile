FROM tomcat:7.0.70-jre8  
MAINTAINER Stefan Oltmann <docker@stefan-oltmann.de>  
  
# Wichtige Parameter setzen  
ENV HOSTNAME stefan-oltmann.de  
ENV TOMCAT_PORT 80  
ENV AUTO_REFRESH false  
ENV USER_ID Stefan  
ENV START_DATUM 2015-01-01  
ENV DISPLAY_AUTH_CODE sichererCodeHoffentlich  
ENV OAUTH2_CLIENT_ID dev.fitbit.com  
ENV FITBIT_CLIENT_SECRET dev.fitbit.com  
  
# Mehr Speicher zugestehen  
ENV JAVA_OPTS -Xmx512m -Xms128m  
  
# Daten als Volume definieren  
VOLUME /root/fitbit_data  
  
# WAR kopieren  
COPY stefans_fitbit_servlet-alpha.war ${CATALINA_HOME}/webapps/fitbit.war

