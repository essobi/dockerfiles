# Dockerfile for WildFly 10  
# Copyright (C) 2017 Kaz Nishimura  
#  
# Copying and distribution of this file, with or without modification,  
# are permitted in any medium without royalty provided the copyright  
# notice and this notice are preserved. This file is offered as-is,  
# without any warranty.  
FROM openjdk:8-jdk  
  
WORKDIR /opt/jboss/wildfly  
  
ENV WILDFLY_VERSION=10.1.0.Final  
  
RUN set -x && \  
wget -q
https://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
&& \  
gzip -d < wildfly-$WILDFLY_VERSION.tar.gz | tar -x --strip-components=1 --no-
same-owner && \  
rm wildfly-$WILDFLY_VERSION.tar.gz  
  
EXPOSE 8080  
ENV LAUNCH_JBOSS_IN_BACKGROUND=1  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0"]  

