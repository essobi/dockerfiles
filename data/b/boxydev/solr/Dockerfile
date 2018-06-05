FROM debian  
MAINTAINER Matthieu Mota <matthieumota@gmail.com>  
  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >>
/etc/apt/sources.list.d/java-8-debian.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty
main" >> /etc/apt/sources.list.d/java-8-debian.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true" | debconf-set-selections  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
oracle-java8-installer \  
oracle-java8-set-default  
  
ADD http://www-eu.apache.org/dist/lucene/solr/6.4.2/solr-6.4.2.tgz /usr/local/  
RUN tar -xzf /usr/local/solr-6.4.2.tgz -C /usr/local  
RUN rm /usr/local/solr-6.4.2.tgz  
  
RUN rm -rf /var/lib/apt/lists/* \  
apt-get clean  
  
EXPOSE 8983  
CMD ["/usr/local/solr-6.4.2/bin/solr", "-f", "-force"]

