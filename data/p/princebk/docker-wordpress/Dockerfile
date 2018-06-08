FROM quay.io/ausnimbus/s2i-php:7.0  
MAINTAINER AusNimbus <support@ausnimbus.com.au>  
  
LABEL io.k8s.description="WordPress quickstart deployment. S2I and scaling to
more than one replica is not supported." \  
io.k8s.display-name="WordPress with Apache 2.4 and PHP 7.0" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="wordpress,php" \  
io.openshift.non-scalable=true  
  
RUN mkdir /opt/app-root/src/wordpress \  
&& fix-permissions /opt/app-root/src/wordpress  
  
COPY s2i/bin/* $STI_SCRIPTS_PATH/  
COPY contrib/* /opt/app-root/src/  
  
VOLUME /opt/app-root/src/wordpress  
CMD $STI_SCRIPTS_PATH/assemble  

