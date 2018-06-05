FROM rodolpheche/wiremock:2.7.1  
  
MAINTAINER pixelcat <aaron@dployr.com>  
  
RUN echo "Installing Wiremock body transformer..."; \  
mkdir -p /var/wiremock/extensions && \  
wget -q https://repo1.maven.org/maven2/com/opentable/wiremock-body-
transformer/1.1.3/wiremock-body-transformer-1.1.3.jar \  
-O /var/wiremock/extensions/wiremock-body-transformer-1.1.3.jar  

