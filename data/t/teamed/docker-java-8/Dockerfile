# rultor container with git, pdd, java 8, maven 3  
FROM ubuntu:14.04  
# repos  
RUN echo "deb http://ppa.launchpad.net/git-core/ppa/ubuntu trusty main" | tee
-a /etc/apt/sources.list  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list  
RUN echo "deb http://ppa.launchpad.net/natecarlson/maven3/ubuntu precise main"
| tee -a /etc/apt/sources.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 E1DF1F24
3DD9F856  
RUN apt-get update  
  
# build-essential  
RUN apt-get install -y build-essential  
  
# git  
RUN apt-get install -y git  
  
# ruby for pdd  
RUN apt-get install -y ruby libmagic1 libmagic-dev ruby-dev  
  
# maven 3  
RUN apt-get install -y maven3  
RUN ln -s /usr/share/maven3/bin/mvn /usr/bin/mvn  
  
# java 8 oracle  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java8-installer ca-certificates  

