# NAME: fahchen/elasticsearch-analysis-ik  
FROM elasticsearch:5.6.7-alpine  
  
MAINTAINER Phil Chen '06fahchen@gmail.com'  
ENV VERSION=5.6.7  
ADD https://github.com/medcl/elasticsearch-analysis-
ik/releases/download/v${VERSION}/elasticsearch-analysis-ik-$VERSION.zip /tmp/  
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install
file:///tmp/elasticsearch-analysis-ik-$VERSION.zip  
  
RUN rm -rf /tm/*  

