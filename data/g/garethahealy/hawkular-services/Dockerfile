FROM docker.io/jboss/base-jdk:8  
MAINTAINER garethahealy (https://github.com/garethahealy/)  
  
LABEL Name="hawkular-services" \  
Vendor="com.garethahealy" \  
Version="0.0.16" \  
License="Apache License, Version 2.0"  
  
# Update to latest packages  
USER root  
RUN yum update -y && \  
yum clean all  
  
# switch back to jboss  
USER 1000  
ENV HAWK_SERVICES_VERSION 0.0.16.Final  
  
# Download Hawkular-Services  
RUN cd $HOME \  
&& curl -L http://origin-
repository.jboss.org/nexus/content/repositories/public/org/hawkular/services/hawkular-
services-dist/$HAWK_SERVICES_VERSION/hawkular-services-
dist-$HAWK_SERVICES_VERSION.zip -o hawkular-services-
dist-$HAWK_SERVICES_VERSION.zip \  
&& bsdtar -xf hawkular-services-dist-$HAWK_SERVICES_VERSION.zip \  
&& rm -f hawkular-services-dist-$HAWK_SERVICES_VERSION.zip \  
&& mv hawkular-services-dist-$HAWK_SERVICES_VERSION hawkular-services-dist  
  
# Add user  
RUN sh $HOME/hawkular-services-dist/bin/add-user.sh -a -u admin -p admin -g
read-write,read-only \  
&& sh $HOME/hawkular-services-dist/bin/add-user.sh -a -u jdoe -p password -g
read-write,read-only  
  
# Expose the ports we're interested in  
EXPOSE 8080  
CMD ["/opt/jboss/hawkular-services-dist/bin/standalone.sh",
"-b","0.0.0.0","-bmanagement","0.0.0.0", "-Dhawkular.rest.user=admin",
"-Dhawkular.rest.password=admin", "-Dhawkular.agent.enabled=true",
"-Dhawkular.metrics.admin-token=awesome_secret_sauce"]  

