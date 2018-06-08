# NAME: fahchen/elasticsearch-analysis-ik  
FROM elasticsearch:5.6.3-alpine  
  
MAINTAINER suxiaolin 'dear.lin@live.com'  
ENV VERSION=5.6.3  
ADD https://github.com/medcl/elasticsearch-analysis-
ik/releases/download/v${VERSION}/elasticsearch-analysis-ik-$VERSION.zip /tmp/  
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install
file:///tmp/elasticsearch-analysis-ik-$VERSION.zip  
  
ADD https://github.com/medcl/elasticsearch-analysis-
pinyin/releases/download/v${VERSION}/elasticsearch-analysis-
pinyin-$VERSION.zip /tmp/  
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install
file:///tmp/elasticsearch-analysis-pinyin-$VERSION.zip  
  
RUN rm -rf /tm/*  

