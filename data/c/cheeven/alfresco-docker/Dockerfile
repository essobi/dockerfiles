FROM centos:latest  
  
MAINTAINER Cheeven Tsai <cheeven@cantab.net>  
  
# Install Linux libraries  
RUN yum -y update && \  
yum -y install epel-release && \  
yum -y install openssh-clients fontconfig libSM libICE libXrender libXext \  
zip unzip curl wget \  
ImageMagick ghostscript \  
tomcat-native.x86_64  
  
# https://wiki.alfresco.com/wiki/Community_file_list_4.2.c  
ENV ALF_DOWNLOAD
http://dl.alfresco.com/release/community/build-04576/alfresco-
community-4.2.c-installer-linux-x64.bin  
ENV ALF_INSTALL_BIN /opt/source/alfresco-community-4.2.c-installer-
linux-x64.bin  
RUN mkdir -p /opt/source && \  
wget -q $ALF_DOWNLOAD -O $ALF_INSTALL_BIN  
  
RUN chmod 755 $ALF_INSTALL_BIN  
  
# http://blyx.com/2014/02/20/alfresco-tip-unattended-installation-with-one-
command/  
RUN $ALF_INSTALL_BIN \  
\--prefix /opt/alfresco \  
\--unattendedmodeui none \  
\--mode unattended \  
\--debuglevel 2 \  
\--enable-components javaalfresco,openofficecomponent \  
\--disable-components postgres,alfrescosharepoint,alfrescogoogledocs \  
\--jdbc_url
"jdbc:postgresql://t450:5432/alfresco?useUnicode=yes&characterEncoding=UTF-8"
\  
\--jdbc_driver org.postgresql.Driver \  
\--jdbc_database alfresco \  
\--jdbc_username postgres \  
\--jdbc_password password \  
\--alfresco_admin_password pass \  
\--baseunixservice_install_as_service 0 \  
\--alfrescocustomstack_services_startup demand  
  
RUN rm -f $ALF_INSTALL_BIN  
  
VOLUME /opt/alfresco/alf_data/contentstore  
  
VOLUME /opt/alfresco/alf_data/contentstore.deleted  
  
VOLUME /opt/alfresco/alf_data/solr/workspace/SpacesStore  
  
VOLUME /opt/alfresco/alf_data/solr/archive/SpacesStore  
  
EXPOSE 8080  
ADD assets/run-alfresco.sh /opt/  
  
CMD /opt/run-alfresco.sh  

