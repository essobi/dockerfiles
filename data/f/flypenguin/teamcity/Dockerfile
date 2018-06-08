FROM java:openjdk-8  
MAINTAINER Axel Bock <mr.axel.bock@gmail.com>  
  
# Please don't change, you'll MOST LIKELY break the container.  
# (except for the version number)  
ENV \  
TEAMCITY_VERSION=9.1.5 \  
TEAMCITY_HOME=/opt/teamcity \  
TEAMCITY_LOGS=/opt/teamcity/logs \  
TEAMCITY_DATA_PATH=/var/lib/teamcity \  
DEBIAN_FRONTEND=noninteractive \  
TEAMCITY_USER_ID=2000 \  
TEAMCITY_GROUP_ID=2000  
RUN mkdir -p ${TEAMCITY_HOME} \  
&& mkdir -p ${TEAMCITY_DATA_PATH} \  
&& groupadd -g ${TEAMCITY_USER_ID} teamcity \  
&& useradd -u ${TEAMCITY_GROUP_ID} -g teamcity -d ${TEAMCITY_DATA_PATH}
teamcity \  
&& curl -sSL -o /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.7/gosu-$(dpkg --print-
architecture)" \  
&& chmod +x /usr/local/bin/gosu  
  
VOLUME ${TEAMCITY_DATA_PATH} ${TEAMCITY_LOGS}  
EXPOSE 8111  
# install teamcity now  
#RUN curl -L http://192.168.119.50:8000/TeamCity-${TEAMCITY_VERSION}.tar.gz \  
RUN curl -L
http://download.jetbrains.com/teamcity/TeamCity-${TEAMCITY_VERSION}.tar.gz \  
| tar xvzf - -C ${TEAMCITY_HOME} \--strip-components=1 \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt /tmp/* /var/tmp/* /var/cache/dpkg /var/cache/apt  
  
# let's do copy at this point, so we can use caching if only the startup
script  
# changes (and we don't have to re-download the TC stuff again)  
COPY start_teamcity.sh /usr/local/bin/  
  
CMD ["/usr/local/bin/start_teamcity.sh"]  

