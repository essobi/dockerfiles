FROM nesslinger/docker-ubuntu-14.04-baseimage:latest  
  
MAINTAINER Michael Neßlinger <Michael.Nesslinger@gmx.de>  
  
RUN sudo apt-get -q update && sudo apt-get -q -y install gettext-base
supervisor apt-transport-https  
  
COPY ./configuration/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# INSTALL FILEBEAT REPO  
RUN curl -s -o key https://artifacts.elastic.co/GPG-KEY-elasticsearch  
RUN sudo apt-key add key  
RUN echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" |
sudo tee -a /etc/apt/sources.list.d/elastic-5.x.list  
  
# Install Java.  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
  
RUN add-apt-repository -y ppa:webupd8team/java  
  
RUN apt-get -q update  
  
RUN apt-get -q -y install -y oracle-java8-installer  
RUN apt-get -q -y install oracle-java8-set-default  
  
RUN update-java-alternatives -s java-8-oracle  
  
# INSTALL FILEBEAT  
RUN sudo apt-get update && sudo apt-get install filebeat  
  
RUN apt-get -q clean  
  
RUN rm -rf /var/lib/apt/lists/*  
RUN rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# Define default command.  
CMD ["/usr/bin/supervisord"]

