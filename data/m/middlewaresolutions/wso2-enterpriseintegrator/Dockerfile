# Use latest openjdk image as the base  
FROM openjdk:8-jdk-alpine  
  
#labels  
LABEL maintainer "emmanuel.lesne@middleware-solutions.fr"  
LABEL version="1.0"  
LABEL description="Image of WSO2 Enterprise Integrator Server."  
LABEL fr.middlewaresolutions.wso2.ei.version="6.1.1"  
LABEL fr.middlewaresolutions.jdk.version="OpenJDK-8"  
  
# Set the EI_VERSION env variable  
ENV EI_VERSION 6.1.1  
ENV EI_HOME /opt/wso2ei-$EI_VERSION  
  
# USER root  
# Add package system  
RUN apk --no-cache add wget  
RUN apk --no-cache add zip  
RUN apk --no-cache add bash  
  
# cf https://github.com/wso2/product-ei/releases  
RUN mkdir /opt && \  
cd /opt && \  
wget https://github.com/wso2/product-
ei/releases/download/v$EI_VERSION/wso2ei-$EI_VERSION.zip && \  
unzip wso2ei-$EI_VERSION.zip  
  
# Expose the ports we're interested in  
EXPOSE 8243 9443 8280  
EXPOSE 9444 9161 7712 7612  
EXPOSE 9445 9765  
EXPOSE 9446 9766 5675 8675 1886 8836 7614  
EXPOSE 9090  
# Set the default command to run on boot  
WORKDIR $EI_HOME  
CMD /opt/wso2ei-$EI_VERSION/bin/integrator.sh  

