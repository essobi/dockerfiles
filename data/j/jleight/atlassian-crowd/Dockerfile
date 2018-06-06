FROM jleight/atlassian-base:latest  
MAINTAINER Jonathon Leight <jonathon.leight@jleight.com>  
  
ENV APP_VERSION 2.8.3  
ENV APP_BASEURL ${ATL_BASEURL}/crowd/downloads/binary  
ENV APP_PACKAGE atlassian-crowd-${APP_VERSION}.tar.gz  
ENV APP_URL ${APP_BASEURL}/${APP_PACKAGE}  
ENV APP_PROPS crowd-webapp/WEB-INF/classes/crowd-init.properties  
  
RUN set -x \  
&& curl -kL "${APP_URL}" | tar -xz -C "${ATL_HOME}" \--strip-components=1 \  
&& chown -R "${ATL_USER}":"${ATL_USER}" "${ATL_HOME}" \  
&& chmod -R 755 "${ATL_HOME}/apache-tomcat/temp" \  
&& chmod -R 755 "${ATL_HOME}/apache-tomcat/logs" \  
&& chmod -R 755 "${ATL_HOME}/apache-tomcat/work" \  
&& echo -e "\ncrowd.home=${ATL_DATA}" >> "${ATL_HOME}/${APP_PROPS}"  
  
ADD crowd-service.sh /opt/crowd-service.sh  
  
EXPOSE 8095  
CMD ["/opt/crowd-service.sh"]  

