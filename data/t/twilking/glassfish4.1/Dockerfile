FROM ubuntu:14.04.2  
MAINTAINER Tim Wilking (tim.wilking@isst.fraunhofer.de)  
  
# Ubuntu  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN apt-get install -y curl  
RUn apt-get install -y unzip  
  
# Oracle JDK 8  
RUN add-apt-repository ppa:webupd8team/java  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get update  
RUN apt-get install -y oracle-java8-installer  
  
# Glassfish  
RUN adduser --disabled-password --disabled-login glassfish  
RUN echo "glassfish:glassfish" | chpasswd && adduser glassfish sudo  
USER glassfish  
  
RUN curl -L -o /tmp/glassfish-4.1.zip
http://download.java.net/glassfish/4.1/release/glassfish-4.1.zip  
RUN unzip /tmp/glassfish-4.1.zip -d $HOME/glassfish4.1  
RUN rm -f /tmp/glassfish-4.1.zip  
  
#Change User to root  
USER root  
  
# Expose WildFly Ports  
EXPOSE 8080  
EXPOSE 4848  
EXPOSE 8181  
# Set the default command to run on boot  
CMD ["home/glassfish/glassfish4.1/glassfish4/bin/asadmin","start-domain","--
verbose"]  

