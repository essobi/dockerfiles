FROM jleight/atlassian-base:latest  
MAINTAINER Jonathon Leight <jonathon.leight@jleight.com>  
  
USER root:root  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
USER "${ATL_USER}":"${ATL_USER}"  
ENV APP_VERSION 3.10.0  
ENV APP_BASEURL ${ATL_BASEURL}/stash/downloads/binary  
ENV APP_PACKAGE atlassian-stash-${APP_VERSION}.tar.gz  
ENV APP_URL ${APP_BASEURL}/${APP_PACKAGE}  
  
RUN set -x \  
&& curl -kL "${APP_URL}" | tar -xz -C "${ATL_HOME}" \--strip-components=1 \  
&& mkdir -p "${ATL_HOME}/conf/Catalina" \  
&& chmod -R 755 "${ATL_HOME}/temp" \  
&& chmod -R 755 "${ATL_HOME}/logs" \  
&& chmod -R 755 "${ATL_HOME}/work" \  
&& chmod -R 755 "${ATL_HOME}/conf/Catalina"  
  
ADD stash-service.sh /opt/stash-service.sh  
  
EXPOSE 7990  
EXPOSE 7999  
CMD ["/opt/stash-service.sh"]  

