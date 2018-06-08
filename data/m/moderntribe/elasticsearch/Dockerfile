FROM elasticsearch:2.3  
  
MAINTAINER Modern Tribe  
  
# install analysis plugins  
RUN /usr/share/elasticsearch/bin/plugin install analysis-icu \  
&& /usr/share/elasticsearch/bin/plugin install analysis-kuromoji \  
&& /usr/share/elasticsearch/bin/plugin install analysis-smartcn

