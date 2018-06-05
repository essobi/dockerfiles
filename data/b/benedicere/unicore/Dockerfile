FROM openjdk:8-jre-alpine  
MAINTAINER Benedikt von St. Vieth  
  
# allow to use https urls in wget and tar with stripping the first directory.  
RUN apk --no-cache add bash openssl python && apk --no-cache --update add tar  
  
# get unicore, extract it, configure it.  
RUN wget -q -O '/unicore.tgz' 'https://unicore-dev.zam.kfa-juelich.de/release-
candidates/core/unicore-servers-7.8.0.tgz' && \  
mkdir -p '/opt/unicore' && \  
tar -xzf /unicore.tgz -C /opt/unicore --strip-components 1 && \  
rm -rf /unicore.tgz /opt/unicore/docs && \  
cd /opt/unicore && \  
sed -i 's/gwHost=hostname/gwHost=0.0.0.0/' configure.properties && \  
sed -i 's/registry=false/registry=true/' configure.properties && \  
sed -i 's/tsi=true/tsi=false/' configure.properties && \  
sed -i 's/uxGatewayHost=${gwHost}/uxGatewayHost=WSRFLITEURL/'
configure.properties && \  
sed -i 's/registryGatewayHost=${gwHost}/registryGatewayHost=WSRFLITEURL/'
configure.properties  
  
ADD entrypoint.sh /entrypoint.sh  
CMD /entrypoint.sh  
  
# default gateway port  
EXPOSE 8080  
# it is not required because we are in the container context, but maybe we
will use it somewhen  
#RUN useradd -s /bin/nologin unicore && chown -R unicore:unicore /opt/unicore  
#USER unicore  

