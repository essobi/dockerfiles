FROM ubuntu:latest  
MAINTAINER Tim <tim@midokura.com>  
  
# Install zookeeper and requirements from repos  
RUN apt-get update && apt-get install -qqy --no-install-recommends
openjdk-7-jre-headless  
RUN apt-get install -qqy zookeeper curl wget vim fish  
  
# Grab confd and set it up  
RUN wget
https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-
amd64  
RUN chmod +x ./confd-0.10.0-linux-amd64  
RUN mv ./confd-0.10.0-linux-amd64 /usr/local/bin/confd  
  
ADD https://raw.githubusercontent.com/midonet/bees/master/confd/bin/confd-
watch-zookeeper /usr/local/bin/confd-watch-zookeeper  
RUN chmod +x /usr/local/bin/confd-watch-zookeeper  
#ADD confd-watch-myid /usr/local/bin/confd-watch-myid  
#RUN chmod +x /usr/local/bin/confd-watch-myid  
ADD https://raw.githubusercontent.com/midonet/bees/master/confd/bin/crappy-
start.sh /usr/share/zookeeper/bin/crappy-start.sh  
RUN chmod +x /usr/share/zookeeper/bin/crappy-start.sh  
  
# Crappy script additions. THIS SHOULD BE REVERTED.  
ADD https://raw.githubusercontent.com/midonet/bees/master/confd/bin/crappy-
script.sh /usr/local/bin/crappy-script  
RUN chmod +x /usr/local/bin/crappy-script  
  
ADD
https://raw.githubusercontent.com/midonet/bees/master/confd/conf.d/zookeeper.toml
/etc/confd/conf.d/zookeeper.toml  
ADD
https://raw.githubusercontent.com/midonet/bees/master/confd/templates/zookeeper.cfg.tmpl
/etc/confd/templates/zookeeper.cfg.tmpl  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
# Add default HOST_IP to localhost  
ENV HOST_IP="localhost"  
  
# Add default HOST_IP to localhost  
ENV HOST_IP="localhost"  
  
VOLUME ["/var/lib/zookeeper", "/tmp/zookeeper"]  
  
WORKDIR /var/lib/zookeeper  
  
EXPOSE 2181 2888 3888  
  
ENTRYPOINT ["/usr/local/bin/confd-watch-zookeeper"]  
  
#CMD ["start-foreground"]  

