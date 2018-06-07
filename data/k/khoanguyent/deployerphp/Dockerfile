FROM php:alpine  
LABEL maintainer="Khoa Nguyen <khoa.tan.nguyen.96@gmail.com"  
  
ARG DEPLOYER_VER=v6.0.0  
ENV DEPLOYER_CHECKSUM=674db6c53b40818d0a2eede4003d3b67a0ce9f99  
  
# Install SSH Client and CA Certificates  
RUN apk add --no-cache ca-certificates openssh-client  
  
# Download and Install Deployer from deployer.org  
RUN curl --silent --show-error --location --output /tmp/dep
https://deployer.org/releases/${DEPLOYER_VER}/deployer.phar \  
&& echo "${DEPLOYER_CHECKSUM} /tmp/dep" | sha1sum -c - \  
&& mv /tmp/dep /usr/bin/dep \  
&& chmod +x /usr/bin/dep  

