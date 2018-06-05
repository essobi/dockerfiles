FROM ubuntu:14.04  
MAINTAINER Basil Kohler<basil.kohler@gmail.com>  
  
# add community-maintained universe repository to sources  
RUN sed -i.bak 's/main$/main universe/' /etc/apt/sources.list  
# date packages were last updated  
ENV REFRESHED_AT 2014-01-14  
ENV DEBIAN_FRONTEND noninteractive  
# resynchronize package index files from their sources  
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
  
RUN apt-get install -y libssl-dev build-essential wget  
RUN apt-get -qq -y install pandoc  
RUN wget http://dl.bintray.com/sbt/debian/sbt-0.13.5.deb  
RUN dpkg -i sbt-0.13.5.deb  
  
ADD . /var/nfn-scala/  
  
WORKDIR /var/nfn-scala  
  
ENV USE_NFN 1  
RUN cd /var/nfn-scala/ccn-lite-nfn/src && make clean all  
# RUN rm /var/nfn-scala/target/scala-2.10/nfn-assembly-0.1-SNAPSHOT.jar  
RUN sbt assembly  
  
EXPOSE 9000/udp  
EXPOSE 9001/udp  
  
ENV CCNL_NAME /docker/nfn  
ENV CCNL_PORT 9000  
ENV CCNL_MGMT_SOCK /tmp/ccn-lite-mgmt.sock  
ENV NFN_SCALA_PORT 9001  
# When linking one container to another, the exposed port information is
transmitted and stored in env variables  
# The CCN-Lite container exposes the udp port 9000.  
# Results in: java -jar /var/nfn-scala/target/scala-2.10/nfn-
assembly-0.1-SNAPSHOT.jar "/docker/nfn" "/tmp/ccn-lite-mgmt.sock"
"127.0.0.1:9000" "9001" "no" "debug"  
CMD java -jar /var/nfn-scala/target/scala-2.10/nfn-assembly-0.1-SNAPSHOT.jar
-m "$CCNL_MGMT_SOCK" -o "$CCNL_PORT" -p "$NFN_SCALA_PORT" -d "$CCNL_NAME"  

