FROM ubuntu:trusty  
MAINTAINER dingmingk <dingmingk@gmail.com>  
  
RUN cp -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
RUN apt-get update -y \  
&& apt-get remove -y openjdk* \  
&& apt-get install -y software-properties-common curl bzip2 unzip xz-utils \  
&& add-apt-repository ppa:webupd8team/java -y \  
&& apt-get update -y \  
&& echo oracle-java6-installer shared/accepted-oracle-license-v1-1 select true
| /usr/bin/debconf-set-selections \  
&& apt-get install -y oracle-java6-installer \  
&& apt-get install -y oracle-java6-set-default \  
&& apt-get remove software-properties-common -y \  
&& apt-get autoremove -y \  
&& apt-get clean  
  
ENV JAVA_HOME /usr/lib/jvm/java-6-oracle  
ENV JAVA_OPTS -Duser.timezone=Asia/Shanghai  
ENV LANG C.UTF-8  

