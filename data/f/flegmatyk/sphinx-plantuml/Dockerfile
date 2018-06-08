FROM anapsix/alpine-java  
MAINTAINER Michał Rudowicz <michal.rudowicz@fl9.eu>  
  
ENV PLANTUML_VERSION 1.2018.1  
ENV LANG en_US.UTF-8  
RUN apk add --no-cache graphviz ttf-droid ttf-droid-nonlatin curl py2-pip
python-dev make \  
&& mkdir /app \  
&& curl -L
https://sourceforge.net/projects/plantuml/files/plantuml.${PLANTUML_VERSION}.jar/download
-o /app/plantuml.jar \  
&& apk del curl \  
&& pip install sphinx==1.6.7 sphinxcontrib-plantuml recommonmark  
  

