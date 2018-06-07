FROM java:7-jre  
  
# locale for tokyo  
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# grab gosu for easy step-down from root  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
46095ACC8548582C1A2699A9D27D666CD88E42B4  
  
ENV ELASTICSEARCH_VERSION 1.5.2  
RUN echo "deb
http://packages.elasticsearch.org/elasticsearch/${ELASTICSEARCH_VERSION%.*}/debian
stable main" > /etc/apt/sources.list.d/elasticsearch.list  
  
RUN apt-get update \  
&& apt-get install elasticsearch=$ELASTICSEARCH_VERSION  
  
# plugins  
RUN /usr/share/elasticsearch/bin/plugin -install mobz/elasticsearch-head  
RUN /usr/share/elasticsearch/bin/plugin -install polyfractal/elasticsearch-
inquisitor  
RUN /usr/share/elasticsearch/bin/plugin -install elasticsearch/elasticsearch-
analysis-kuromoji/2.5.0  
  
# set kuromoji to default analyzer  
RUN echo "index.analysis.analyzer.default.type: custom" >>
/etc/elasticsearch/elasticsearch.yml  
RUN echo "index.analysis.analyzer.default.tokenizer: kuromoji_tokenizer" >>
/etc/elasticsearch/elasticsearch.yml  
  
ENV PATH /usr/share/elasticsearch/bin:$PATH  
  
VOLUME ["/usr/share/elasticsearch/data", "/usr/share/elasticsearch/"]  
  
EXPOSE 9300  
EXPOSE 9200  
ENTRYPOINT ["/usr/share/elasticsearch/bin/elasticsearch"]  

