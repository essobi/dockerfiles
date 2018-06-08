# Use latest Alpine Linux as the base image.  
FROM alpine:latest  
  
# Once Alpine Linux is booted up, run a full update and install 'build-base',
'wget' and 'Java Runtime Environment (OpenJDK) 8'  
RUN apk update && apk add --no-cache build-base wget openjdk8  
  
# Create an OpenDaylight (ODL) parent directory in /opt.  
RUN mkdir /opt  
RUN mkdir /opt/odl  
  
# Download ODL Nitrogen release from the OpenDaylight website, and save it as
'odl.tar.gz' in /opt/odl.  
RUN wget -O /opt/odl/odl.tar.gz \  
https://nexus.opendaylight.org/content/repositories/public/org/opendaylight/integration/karaf/0.7.1/karaf-0.7.1.tar.gz  
  
# Extract the contents of 'odl.tar.gz' inside directory /opt/odl.  
RUN tar -xzf /opt/odl/odl.tar.gz -C /opt/odl  
  
# The contents of '' will get extracted into a directory named
'/opt/odl/karaf-0.7.1' ...  
# Let's rename it to '/opt/odl/nitrogen'.  
RUN mv /opt/odl/karaf-* /opt/odl/nitrogen  
  
# Expose ports 8101 (Karaf CLI) and 8181 (Web UI & REST API)  
EXPOSE 8101 8181  
# Install some prerequisite ODL features, including DLUX (Web UI), NETCONF-
over-SSH and the RESTCONF API. Modify  
# 'featuresBoot' setting in 'etc/org.apache.karaf.features.cfg' with comma-
separated list of features to install at startup.  
RUN sed -i -e '/standard, \\\/{N;d;}' \  
-e 's/featuresBoot =.*/featuresBoot = odl-dluxapps-applications,odl-netconf-connector-ssh,odl-restconf,standard,wrap/g' \  
/opt/odl/nitrogen/etc/org.apache.karaf.features.cfg  
  
# Start ODL Karaf (as a background process)  
CMD /opt/odl/nitrogen/bin/karaf  

