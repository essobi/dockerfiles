FROM ELASTICSEARCH:1.7  
MAINTAINER Dogstudio <devs@dogstudio.be>  
  
RUN USERMOD -U 1000 ELASTICSEARCH  
RUN usermod -a -G users elasticsearch  
  
RUN /usr/share/elasticsearch/bin/plugin install "elasticsearch/elasticsearch-
analysis-icu/2.7.0"  
RUN /usr/share/elasticsearch/bin/plugin install "jettro/elasticsearch-gui"  
# http://nawak.dok/service/search/refresh > Generate Index Mapping  

