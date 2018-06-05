FROM ubuntu:14.04  
MAINTAINER Albert Alvarez  
  
RUN locale-gen es_ES.UTF-8  
ENV LANG='es_ES.UTF-8' LANGUAGE='es_ES:es' LC_ALL='es_ES.UTF-8'  
# Install  
#RUN apt-get update && apt-get upgrade -y && apt-get install -y supervisor
wget  
RUN apt-get update && apt-get upgrade -y && apt-get install -y wget  
RUN apt-get install software-properties-common -y  
#RUN add-apt-repository -y ppa:webupd8team/java  
#RUN apt-get update  
#RUN echo debconf shared/accepted-oracle-license-v1-1 select true | sudo
debconf-set-selections  
#RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo
debconf-set-selections  
#RUN apt-get -y install oracle-java8-installer  
RUN apt-get install -y openjdk-7-jre openjdk-7-jdk  
RUN add-apt-repository -y ppa:vajdics/netbeans-installer  
RUN apt-get update  
RUN apt-get install unzip -y  
RUN apt-get install netbeans-installer -y  
RUN mkdir /root/.netbeans /root/.netbeans/8.1 /root/.netbeans/8.1/var  
RUN touch /root/.netbeans/8.1/var/license_accepted  
ENTRYPOINT ["/opt/netbeans/bin/netbeans"]  
#CMD ["--tail-log"]  

