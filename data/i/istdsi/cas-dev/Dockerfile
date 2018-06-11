FROM sergiofbsilva/cas-dev:latest  
  
MAINTAINER David Martinho  
  
COPY pom.xml /cas-overlay  
COPY cas.properties /etc/cas/cas.properties  
COPY HTTP-10000003.json /cas-overlay/src/main/resources/services/  
COPY deployerConfigContext.xml /cas-overlay/src/main/webapp/WEB-INF/  
RUN ln -s /config/people.txt /cas-overlay/src/main/resources/people.txt  
  
VOLUME ["/config"]  
  
CMD "/cas-overlay/bin/run-jetty.sh"

