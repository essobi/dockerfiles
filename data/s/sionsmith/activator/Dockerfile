FROM sionsmith/scala-2-11  
MAINTAINER Sion Smith sion.smith@gmail.com  
  
RUN apt-get -y install wget unzip && apt-get clean  
  
# Activator install  
RUN wget http://downloads.typesafe.com/typesafe-activator/1.2.10/typesafe-
activator-1.2.10-minimal.zip -O /opt/activator.zip  
  
RUN unzip /opt/activator.zip -d /opt  
  
RUN mv /opt/activator-1.2.10-minimal /opt/activator  
RUN rm /opt/activator.zip  
  
ENV PATH /opt/activator:$PATH  

