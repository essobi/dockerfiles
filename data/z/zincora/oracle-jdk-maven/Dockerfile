# Uses circleci base  
# Removes openjdk  
# keeps existing toolset (maven 3.5.0, git, etc)  
# Installs:  
# Oracle Java 1.8.0_141 64 bit  
FROM circleci/openjdk:8-jdk  
  
MAINTAINER Zincora (https://bitbucket.org/zincora/docker-oracle-jdk-maven)  
  
# set shell variables for java installation  
ENV jvm_path /usr/lib/jvm  
ENV old_path $jvm_path/java-8-openjdk-amd64  
ENV java_version 1.8.0_141  
ENV filename jdk-8u141-linux-x64.tar.gz  
ENV downloadlink http://download.oracle.com/otn-
pub/java/jdk/8u141-b15/336fa29ff2bb4ef291e347e091f7f4a7/$filename  
  
  
# download java, accepting the license agreement  
RUN wget --no-cookies --header "Cookie: oraclelicense=accept-securebackup-
cookie" -O /tmp/$filename $downloadlink  
  
RUN sudo rm -r $old_path  
  
# unpack java  
RUN sudo tar -zxf /tmp/$filename -C $jvm_path  
RUN sudo ln -s $jvm_path/jdk$java_version $old_path  
  
#install heroku  
RUN wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh  
  
CMD ["/bin/bash"]  
  

