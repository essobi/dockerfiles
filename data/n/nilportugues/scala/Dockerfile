FROM phusion/baseimage  
  
CMD ["/sbin/my_init"]  
  
##Oracle Java 8  
RUN echo -e "\n" | add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java8-installer wget  
  
## Java 8 Environment  
RUN apt-get install -y oracle-java8-set-default  
  
## chat  
RUN wget www.scala-lang.org/files/archive/scala-2.11.7.deb  
RUN dpkg -i scala-2.11.7.deb  
RUN apt-get update -y  
RUN apt-get install -y wget  
  
## chat-sbt  
RUN echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a
/etc/apt/sources.list.d/sbt.list  
RUN sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823  
RUN sudo apt-get update  
RUN sudo apt-get install -y sbt  
  
WORKDIR /var/www  
EXPOSE 9000  

