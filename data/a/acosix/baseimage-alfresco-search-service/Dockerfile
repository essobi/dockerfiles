FROM acosix/baseimage-jdk8:latest  
  
LABEL vendor="Acosix GmbH" \  
de.acosix.version="0.0.1-SNAPSHOT" \  
de.acosix.is-beta="" \  
de.acosix.is-production="" \  
de.acosix.release-date="2017-06-09" \  
de.acosix.maintainer="axel.faust@acosix.de"  
  
ENV RMI_PORT=5003  
  
EXPOSE 8983 5003  
  
# having SOLR core configurations in an externalised volume is optional -
index is expected to be always externalised  
VOLUME ["/srv/alfresco-search-services/index", "/srv/alfresco-search-
services/coreConfigs"]  
  
# Need wget/unzip for lazy download+install (a more specialized image may
decide to pre-package ASS)  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update -q \  
&& apt-get upgrade -q -y -o Dpkg::Options::="--force-confdef" -o
Dpkg::Options::="--force-confold" \  
&& apt-get install -q -y -o Dpkg::Options::="--force-confdef" -o
Dpkg::Options::="--force-confold" \  
wget \  
unzip \  
lsof \  
&& addgroup --system solr \  
&& adduser --system \--shell /bin/bash --disabled-password --no-create-home
--ingroup solr solr \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# add prepared files that would be too awkward to handle via RUN / sed  
COPY initASS.sh startASS.sh ASS-logrotate.d /tmp/  
  
RUN mv /tmp/ASS-logrotate.d /etc/logrotate.d/alfresco-search-services \  
&& mkdir -p /etc/my_init.d \  
&& mv /tmp/initASS.sh /etc/my_init.d/20_initAlfrescoSearchServices.sh \  
&& chmod +x /etc/my_init.d/20_initAlfrescoSearchServices.sh \  
&& mkdir /etc/service/alfresco-search-services \  
&& mv /tmp/startASS.sh /etc/service/alfresco-search-services/run \  
&& chmod +x /etc/service/alfresco-search-services/run \  

