# Base image  
FROM java:7-jre  
  
# Maintainer  
MAINTAINER Ivo Krooswijk "ivo@krooswijk.com"  
# Set last version  
ENV NUTCH_VERSION "1.14"  
# Set java env Variable  
ENV JAVA_HOME /usr  
  
# Download nutch  
RUN wget http://ftp.tudelft.nl/apache/nutch/$NUTCH_VERSION/apache-
nutch-$NUTCH_VERSION-bin.zip  
  
# Set nutch directory  
#ENV NUTCH_ROOT /nutch-$NUTCH_VERSION  
# Unzip Apache Nutch and move to nutch root  
RUN unzip apache-nutch-$NUTCH_VERSION-bin.zip  
RUN rm apache-nutch-$NUTCH_VERSION-bin.zip  
RUN mv apache-nutch-$NUTCH_VERSION/ /nutch  
  
# Add configurations  
ADD conf/nutch-site.xml /nutch/conf/nutch-site.xml  
ADD conf/regex-urlfilter.txt /nutch/conf/regex-urlfilter.txt  
  
# Add seed with urls  
RUN mkdir -p /nutch/urls  
ADD urls/seed.txt /nutch/urls/seed.txt  
  
# Data volume for nutch  
VOLUME ["/data"]  
  
# Set workdir to nutch folder  
WORKDIR /nutch  
  
# Nutch server port  
EXPOSE 8899  

