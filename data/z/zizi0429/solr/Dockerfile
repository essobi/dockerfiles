FROM centos:6  
  
RUN yum install -y java lsof  
RUN curl -O
"http://ftp.jaist.ac.jp/pub/apache/lucene/solr/6.0.0/solr-6.0.0.tgz"  
RUN tar -xvf solr-6.0.0.tgz  
WORKDIR ./solr-6.0.0  
COPY default server/solr/default  
  
EXPOSE 8983  
CMD ["bin/solr", "start", "-f", "-p", "8983"]  

