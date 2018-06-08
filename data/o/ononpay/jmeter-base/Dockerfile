# Use JDK-8 on alpine.  
From openjdk:8-alpine  
  
# Origined from https://hub.docker.com/r/famiko/jmeter-base/  
# Modified to match with OnOnpay software development platform  
MAINTAINER Duong Dinh Cuong <dinhcuong@ononpay.com>  
  
ENV JMETER_VERSION 3.3  
# Install Pre-requisite Packages like wget  
RUN apk update && apk add wget unzip  
  
# Installing jmeter  
RUN mkdir /jmeter \  
&& cd /jmeter/ \  
&& wget https://archive.apache.org/dist/jmeter/binaries/apache-
jmeter-$JMETER_VERSION.tgz \  
&& tar -xzf apache-jmeter-$JMETER_VERSION.tgz \  
&& rm apache-jmeter-$JMETER_VERSION.tgz  
  
# Setting Jmeter Home  
ENV JMETER_HOME /jmeter/apache-jmeter-$JMETER_VERSION/  
  
# Finally Adding Jmeter to the Path  
ENV PATH $JMETER_HOME/bin:$PATH  
  
COPY ./bin $JMETER_HOME/bin  
COPY ./entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
WORKDIR /perftests/  
  
CMD ["/entrypoint.sh"]

