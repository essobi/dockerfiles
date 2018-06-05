FROM java:8  
MAINTAINER TIS Inc.  
  
RUN apt-get update -y \  
&& apt-get install -y -q curl  
  
ENV APACHE_APOLLO_VERSION 1.7.1  
ENV APACHE_APOLLO_HOME /opt/apache-apollo  
ENV APACHE_APOLLO_USER apollo  
  
# Install Apache Apollo  
WORKDIR /tmp  
  
RUN curl -s -o apache-apollo.tar.gz \  
http://archive.apache.org/dist/activemq/activemq-
apollo/$APACHE_APOLLO_VERSION/apache-apollo-$APACHE_APOLLO_VERSION-unix-
distro.tar.gz \  
&& mkdir -p $APACHE_APOLLO_HOME \  
&& tar xzf apache-apollo.tar.gz -C $APACHE_APOLLO_HOME \--strip-components=1 \  
&& rm apache-apollo.tar.gz \  
&& useradd -r -M -d $APACHE_APOLLO_HOME $APACHE_APOLLO_USER \  
&& chown -R $APACHE_APOLLO_USER:$APACHE_APOLLO_USER $APACHE_APOLLO_HOME  
  
# Clean up  
RUN apt-get remove -y --purge wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Creating a Broker Instance  
WORKDIR /var/lib  
  
RUN $APACHE_APOLLO_HOME/bin/apollo create broker  
  
EXPOSE 61680  
EXPOSE 61681  
EXPOSE 61613  
EXPOSE 61614  
EXPOSE 61623  
EXPOSE 61624  
ENTRYPOINT ["/var/lib/broker/bin/apollo-broker", "run"]  

