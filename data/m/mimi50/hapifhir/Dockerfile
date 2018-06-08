FROM docker.io/centos  
RUN yum install -y --setopt=tsflags=nodocs java-1.8.0-openjdk-headless which
tar bzip2 ;\  
yum clean all  
ARG hfVer=3.1.0  
ADD https://github.com/jamesagnew/hapi-fhir/releases/download/v${hfVer}/hapi-
fhir-${hfVer}-cli.tar.bz2 /opt  
RUN mkdir /opt/hapi-fhir; cd /opt/hapi-fhir ;\  
tar -jxvf /opt/hapi-fhir-${hfVer}-cli.tar.bz2 ;\  
rm -f /opt/hapi-fhir-${hfVer}-cli.tar.bz2  
  
EXPOSE 8080  
CMD /bin/bash -c 'cd /opt/hapi-fhir ; ./hapi-fhir-cli run-server -f dstu3'  

