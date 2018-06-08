FROM ohtake/ubuntu1404-ansible-ruby:latest  
  
MAINTAINER ohtake<manabu.ohtake.297@gmail.com>  
  
RUN apt-get install -y software-properties-common  
RUN apt-add-repository ppa:webupd8team/java  
RUN apt-get update -y  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 boolean
true" | debconf-set-selections  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get install -y oracle-java8-installer wget git curl unzip language-
pack-ja python2.7 g++ build-essential rsync  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle/jre  
  
RUN wget https://services.gradle.org/distributions/gradle-2.4-all.zip  
RUN unzip gradle-2.4-all.zip && mv gradle-2.4 /opt  
  
RUN wget git.io/nodebrew  
RUN perl nodebrew setup  
ENV PATH /root/.nodebrew/current/bin:/opt/gradle-2.4/bin:$JAVA_HOME/bin:$PATH  
ADD ./versions.txt /root/versions.txt  
RUN /bin/bash -l -c 'xargs -L 1 nodebrew install-binary < /root/versions.txt'  
  
RUN /bin/bash -l -c 'for v in $(cat /root/versions.txt); do nodebrew use $v;
done'  
RUN /bin/bash -l -c 'npm install -g gulp bower node-gyp coffee-script'  

