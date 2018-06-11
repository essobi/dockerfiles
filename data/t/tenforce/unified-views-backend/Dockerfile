FROM java:8-jre-alpine  
  
MAINTAINER Erika Pauwels <erika.pauwels@tenforce.com>  
MAINTAINER Bert Van Nuffelen <bert.van.nuffelen@tenforce.com>  
  
RUN apk add --no-cache bash  
  
ENV UNIFIED_VIEWS_VERSION 3.0.0  
ADD
http://repository.unifiedviews.eu/nexus/content/repositories/releases/eu/unifiedviews/backend/3.0.0/backend-3.0.0.jar
/backend.jar  
  
ADD startup.sh /bin  
RUN chmod +x /bin/startup.sh  
  
EXPOSE 5001  
WORKDIR /unified-views  
CMD /bin/startup.sh  

