FROM owncloud/base:latest  
MAINTAINER ownCloud DevOps <devops@owncloud.com>  
  
ARG VERSION  
ARG BUILD_DATE  
ARG VCS_REF  
  
ARG TARBALL  
#ARG RICHDOCUMENTS  
RUN curl -sLo - ${TARBALL} | tar xfj - -C /var/www/  
#ADD owncloud-${VERSION}.tar.bz2 /var/www/  
# RUN curl -sLo - ${RICHDOCUMENTS} | tar xfz - -C /var/www/owncloud/apps/ && \  
# mv /var/www/owncloud/apps/richdocuments-*
/var/www/owncloud/apps/richdocuments  
RUN find /var/www/owncloud \\( \\! -user www-data -o \\! -group www-data \\)
-print0 | xargs -r -0 chown www-data:www-data  
  
#install clamAV for antivirus support in owncloud  
RUN apt-get update && \  
apt-get install -y \  
clamav \  
clamav-daemon \  
&& apt-get clean  
  
#Activate antivirus app & customize skeleton files  
ADD ./etc/owncloud.d/*.sh /etc/owncloud.d/  
#update clamAV DB on startup  
ADD ./etc/entrypoint.d/*.sh /etc/entrypoint.d/  
#CRON update task  
ADD ./etc/cron.d/* /etc/cron.d/  
  
LABEL org.label-schema.version=$VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE  
LABEL org.label-schema.vcs-ref=$VCS_REF  
LABEL org.label-schema.vcs-url="https://github.com/owncloud-docker/server.git"  
LABEL org.label-schema.name="ownCloud Server"  
LABEL org.label-schema.vendor="ownCloud GmbH"  
LABEL org.label-schema.schema-version="1.0"  

