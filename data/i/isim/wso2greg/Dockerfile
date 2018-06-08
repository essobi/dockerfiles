FROM isim/oraclejava:1.8.0_101  
MAINTAINER Ivan Sim, ihcsim@gmail.com  
  
ARG GREG_VERSION=${GREG_VERSION:-5.3.0}  
ARG VCS_REF  
LABEL org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/ihcsim/docker-wso2greg"  
  
RUN wget -P /opt https://s3-us-
west-2.amazonaws.com/wso2-stratos/wso2greg-$GREG_VERSION.zip && \  
apt-get update && \  
apt-get install -y zip && \  
apt-get clean && \  
unzip /opt/wso2greg-$GREG_VERSION.zip -d /opt && \  
rm /opt/wso2greg-$GREG_VERSION.zip  
  
WORKDIR /opt/wso2greg-$GREG_VERSION  
EXPOSE 9443 9763  
ENTRYPOINT ["bin/wso2server.sh"]  

