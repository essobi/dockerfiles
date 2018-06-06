###############################################################################################  
# Dockerfile used to create WildFly container image.  
#  
# See README.md  
###############################################################################################  
  
FROM rahuljain/openjdk:8u161  
  
LABEL maintainer="rahuljain"  
  
ENV VERSION 12.0.0  
ENV WILDFLY_VERSION=12.0.0 WILDFLY_HOME=/opt/wildfly  
ARG ADMIN_USERNAME=admin  
ARG ADMIN_PASSWORD=admin123  
  
# install libaio and clean apk repository  
RUN apk add --no-cache --update libaio && \  
rm -rf /var/cache/apk/*  
  
# install wildfly  
RUN wget -q
https://download.jboss.org/wildfly/${WILDFLY_VERSION}.Final/wildfly-${WILDFLY_VERSION}.Final.tar.gz
-O - | tar -zx -C /opt && \  
mv /opt/wildfly-${WILDFLY_VERSION}.Final ${WILDFLY_HOME}  
  
# application: 8080, management: 9990  
EXPOSE 8080 9990  
  
# Add user for adminstration purpose  
RUN /opt/wildfly/bin/add-user.sh ${ADMIN_USERNAME} ${ADMIN_PASSWORD} --silent  
  
# Set the default command to run on boot  
# This will boot WildFly in the standalone mode and bind to all interface  
CMD ["/opt/wildfly/bin/standalone.sh", "-b", "0.0.0.0"]  

