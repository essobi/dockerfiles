FROM ubuntu:xenial  
MAINTAINER Javier Vergara <javier.vergara-at-wenuy.com>  
# base  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y curl wget git vim software-properties-common && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
#java  
RUN add-apt-repository ppa:webupd8team/java -y && \  
apt-get update -y && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
#node  
RUN curl -sL https://deb.nodesource.com/setup_5.x > install_node.sh && \  
bash install_node.sh && \  
rm -f install_node.sh && \  
apt-get install -y nodejs && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
#firefox & chrome  
RUN echo 'deb http://downloads.sourceforge.net/project/ubuntuzilla/mozilla/apt
all main' > /etc/apt/sources.list.d/ubuntuzilla.list  
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com C1289A29  
  
RUN curl -sL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - && \  
echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >>
/etc/apt/sources.list.d/google.list && \  
apt-get update && \  
apt-get install -y build-essential xvfb firefox google-chrome-stable && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# wct  
RUN npm install -g web-component-tester bower  

