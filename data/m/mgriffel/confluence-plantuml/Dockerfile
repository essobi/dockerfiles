FROM atlassian/confluence-server:6.7  
  
LABEL Description="This image is used to start Atlassian Confluence with
PlantUML Plugin Support (Graphviz)" Vendor="mgriffel" Version=6.7-1  
  
MAINTAINER mgriffel <michael.griffel@gmail.com>  
  
ENV RUN_USER daemon  
ENV RUN_GROUP daemon  
  
USER root  
  
RUN set -x \  
&& apk update \  
&& apk add \  
ttf-freefont \  
graphviz  
  
USER ${RUN_USER}:${RUN_GROUP}  

