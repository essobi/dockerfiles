FROM ubuntu:trusty  
MAINTAINER finalcut bill@rawlinson.us  
  
# add community-maintained universe repository to sources  
RUN sed -i.bak 's/main$/main universe/' /etc/apt/sources.list  
  
# sync packages from sources  
RUN apt-get -qq update  
  
# install software-properties-common (ubuntu >= 12.10) to be able to use add-
apt-repository  
RUN apt-get -qq -y install software-properties-common  
  
# add PPA for java  
RUN add-apt-repository ppa:webupd8team/java  
  
# resynchronize package index files from their sources  
RUN apt-get -qq update  
  
# accept Oracle license  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
# install jdk7  
RUN apt-get -qq -y install oracle-java7-installer  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
  
  
#install some helper libraries if they arent installed yet  
RUN apt-get -qq -y install ant git curl wget git-core  
  
#necessary ant libs  
ADD ./ant/ /usr/share/ant/lib/  
  
#install jenkins  
RUN wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo
apt-key add -  
RUN echo "deb http://pkg.jenkins-ci.org/debian binary/" >
/etc/apt/sources.list.d/jenkins.list  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y jenkins  
  
ENV JENKINS_HOME /var/lib/jenkins  
RUN chmod -R 777 /var/lib/jenkins/  
  
VOLUME /var/lib/jenkins  
  
# Use bash, not dash  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
EXPOSE 8080  
ADD run /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
  
CMD ["/usr/local/bin/run"]  

