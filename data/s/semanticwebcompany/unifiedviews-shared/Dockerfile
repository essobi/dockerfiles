FROM java:8-jre-alpine  
  
MAINTAINER Niels Vandekeybus <niels.vandekeybus@tenforce.com>  
MAINTAINER Bert Van Nuffelen <bert.van.nuffelen@tenforce.com>  
  
RUN apk add --no-cache bash gawk sed grep bc coreutils unzip  
  
ENV UNIFIED_VIEWS_VERSION 2.3.1  
  
RUN mkdir -p /unified-views/lib  
#ADD packages/lib /unified-views/lib  
ADD
https://repository.unifiedviews.eu/nexus/content/repositories/releases/eu/unifiedviews/backend-
libs/3.0.0/backend-libs-3.0.0.zip /unified-views/lib/backend-libs-3.0.0.zip  
RUN cd /unified-views/lib && unzip backend-libs-3.0.0.zip  
  
RUN mkdir -p /unified-views/dpus/lib  
ADD
https://repository.unifiedviews.eu/nexus/content/repositories/releases/eu/unifiedviews/libs-
core/3.0.0/libs-core-3.0.0.zip /unified-views/dpus/lib/libs-core-3.0.0.zip  
RUN cd /unified-views/dpus/lib && unzip libs-core-3.0.0.zip  
ADD
https://repository.unifiedviews.eu/nexus/content/repositories/releases/eu/unifiedviews/dpu-v2-compatibility-
package/1.0.0/dpu-v2-compatibility-package-1.0.0.jar /unified-
views/dpus/lib/dpu-v2-compatibility-package-1.0.0.jar  
  
ADD config /config  
  
VOLUME /unified-views  
  
RUN chmod +x /config/start.sh && chmod -R 777 /config  
  
ENTRYPOINT ["/config/start.sh"]  

