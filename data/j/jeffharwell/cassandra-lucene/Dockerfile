FROM gcr.io/google-samples/cassandra:v12  
MAINTAINER Jeff Harwell <jeff.harwell@gmail.com>  
  
## This is, of course, non-ideal.  
## If I had the dockerfile for the GCR image I would do this differently  
## Download and install the Lucene Index plugin. The compiled binary is at
www.jeffharwell.com  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get install wget && \  
wget http://www.jeffharwell.com/jars/cassandra-lucene-index-plugin-3.9.0.jar
&& \  
mv ./cassandra-lucene-index-plugin-3.9.0.jar ${CASSANDRA_HOME}/lib/ && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

