FROM billyboingo/docker-baseimage  
MAINTAINER Bill Weiss <billyboingo@gmail.com>  
  
#Setup to auto accept Oracle license  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
  
#Install the required tools  
RUN apt-get -q update && apt-get install -qy --force-yes \  
unzip \  
software-properties-common  
  
#Set JAVA_HOME  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
#Install the JDK  
RUN add-apt-repository ppa:webupd8team/java -y && \  
apt-get -q update && apt-get install -qy --force-yes oracle-java8-installer  
  
#Enable full strength encryption  
ADD ./UnlimitedJCEPolicy.zip /tmp/UnlimitedJCEPolicy.zip  
RUN cd /tmp && \  
unzip UnlimitedJCEPolicy.zip && \  
mv /tmp/UnlimitedJCEPolicy/*.jar $JAVA_HOME/jre/lib/security/  
#Clean up  
RUN apt-get -y autoremove; apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

