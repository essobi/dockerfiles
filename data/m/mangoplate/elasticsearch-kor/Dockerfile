FROM mangoplate/elasticsearch-8-jdk:1.7.3  
ENV ES_VERSION 1.7.3  
ENV ES_PLUGIN_AWS_VERSION 2.7.1  
ENV ES_HOME /usr/share/elasticsearch  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y build-essential  
  
WORKDIR /opt  
  
RUN \  
curl -L -O https://bitbucket.org/eunjeon/mecab-
ko/downloads/mecab-0.996-ko-0.9.2.tar.gz \  
&& tar xvf mecab-0.996-ko-0.9.2.tar.gz  
  
WORKDIR /opt/mecab-0.996-ko-0.9.2  
RUN \  
./configure \  
&& make \  
&& make check \  
&& make install  
  
WORKDIR /opt  
RUN \  
curl -L -O https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-
dic-1.6.1-20140814.tar.gz \  
&& tar zxvf mecab-ko-dic-1.6.1-20140814.tar.gz  
  
WORKDIR /opt/mecab-ko-dic-1.6.1-20140814  
RUN \  
./configure \  
&& ldconfig \  
&& make \  
&& make install  
  
WORKDIR /opt  
RUN \  
curl -L -O https://mecab.googlecode.com/files/mecab-java-0.996.tar.gz \  
&& tar zxvf mecab-java-0.996.tar.gz  
  
WORKDIR /opt/mecab-java-0.996  
COPY Makefile ./  
RUN \  
make \  
&& cp libMeCab.so /usr/local/lib  
  
RUN \  
apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN $ES_HOME/bin/plugin --install analysis-mecab-ko-0.16.1 --url
https://bitbucket.org/eunjeon/mecab-ko-lucene-
analyzer/downloads/elasticsearch-analysis-mecab-ko-0.16.1.zip  
  
ENTRYPOINT ["/docker-entrypoint.sh","-Djava.library.path=/usr/local/lib"]  
  
EXPOSE 9200 9300  
CMD ["elasticsearch"]  

