FROM jenkins:alpine  
  
MAINTAINER Duong Dinh Cuong <dinhcuong@ononpay.com>  
  
USER root  
  
ENV JMETER_VERSION 3.3  
# Setting Jmeter Home  
ENV JMETER_HOME /apache-jmeter-$JMETER_VERSION/  
ENV JENKINS_PREFIX=/  
  
# Finally Adding Jmeter to the Path  
ENV PATH $JMETER_HOME/bin:$PATH  
COPY ./bin $JMETER_HOME/bin  
  
RUN apk --update add wget unzip \  
&& wget http://updates.jenkins-ci.org/latest/performance.hpi \  
&& mkdir -p $HOME/.jenkins/plugins/ && mv performance.hpi
$HOME/.jenkins/plugins/ \  
&& wget https://archive.apache.org/dist/jmeter/binaries/apache-
jmeter-$JMETER_VERSION.tgz \  
&& tar -xzf apache-jmeter-$JMETER_VERSION.tgz \  
&& rm apache-jmeter-$JMETER_VERSION.tgz \  
&& mv $JMETER_HOME/bin/jenkins.sh /usr/local/bin/jenkins.sh \  
&& chmod +x /usr/local/bin/jenkins.sh  
  
USER jenkins

