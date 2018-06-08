FROM noonien/perforce-base  
MAINTAINER George Jiglau <george@mux.ro>  
  
RUN apt-get install -y perforce-cli default-jre-headless  
  
RUN wget -q -O-
http://www.perforce.com/downloads/perforce/r14.1/bin.java/p4search.tgz | tar
zx -C /opt \  
&& mv /opt/p4search-2014.1.828661 /opt/perforce-search \  
&& cd /opt/perforce-search \  
&& mv jetty jetty-config \  
&& tar zxf solr-4.5.1.tgz \  
&& tar zxf jetty-distribution-8.1.14.v20131031.tar.gz \  
&& mv solr-4.5.1 solr \  
&& mv jetty-distribution-8.1.14.v20131031 jetty \  
&& mv solr-config/4.5.1/schema.xml solr/example/solr/collection1/conf \  
&& mv scripts/solr-control.sh solr/example \  
&& rm -rf jetty/webapps/* jetty/contexts/* \  
&& mv p4-search*.war jetty/webapps/p4-search.war \  
&& mv jetty-config/contexts/*.xml jetty/contexts \  
&& mv conf/search.config jetty/resources \  
&& mv scripts/p4search-control.sh jetty \  
&& rm -rf conf jetty-* solr-* scripts install.sh  
  
COPY run.sh /  
CMD ["/run.sh"]  
  

