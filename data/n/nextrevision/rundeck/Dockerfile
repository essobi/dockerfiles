FROM ubuntu:trusty  
  
RUN apt-get update && \  
apt-get install -y wget \  
openjdk-7-jre-headless  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /rundeck/libext  
  
WORKDIR /rundeck  
  
RUN wget --quiet -O rundeck-launcher-2.6.2.jar \  
http://dl.bintray.com/rundeck/rundeck-maven/rundeck-launcher-2.6.2.jar  
  
RUN java -jar rundeck-launcher-2.6.2.jar --installonly  
  
COPY files/install_plugins.sh /usr/local/bin  
RUN chmod +x /usr/local/bin/install_plugins.sh  
  
COPY files/plugins.txt /rundeck/plugins.txt  
RUN /usr/local/bin/install_plugins.sh  
  
COPY files/rundeck_startup.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/rundeck_startup.sh  
  
CMD /usr/local/bin/rundeck_startup.sh  

