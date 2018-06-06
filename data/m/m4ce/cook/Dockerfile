FROM centos:7  
MAINTAINER Matteo Cerutti <matteo.cerutti@hotmail.co.uk>  
  
# install java and maven  
RUN yum install -y java-1.8.0 maven wget unzip git -y  
  
# prepare dest directory  
RUN mkdir -p /opt/Cook/{bin,etc,src}  
  
# downlod lein  
RUN wget
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein -O
/usr/bin/lein  
RUN chmod +x /usr/bin/lein  
  
# download datomic-free  
RUN wget https://my.datomic.com/downloads/free/0.9.5394 -O /tmp/datomic-
free-0.9.5394.zip  
RUN unzip /tmp/datomic-free-0.9.5394.zip -d /tmp  
RUN cd /tmp/datomic-free-0.9.5394 && ./bin/maven-install  
  
# build JARs  
RUN mkdir -p /opt/Cook/src/scheduler  
ADD scheduler /opt/Cook/src/scheduler  
ENV LEIN_ROOT ""  
RUN cd /opt/Cook/src/scheduler && /usr/bin/lein uberjar  
  
# move JARs  
RUN mv /opt/Cook/src/scheduler/target/*-SNAPSHOT.jar /opt/Cook/bin/cook.jar  
RUN mv /opt/Cook/src/scheduler/target/*-SNAPSHOT-standalone.jar
/opt/Cook/bin/cook-standalone.jar  
  
# remove source  
RUN rm -rf /opt/Cook/src  
RUN rpm -ivh http://repos.mesosphere.com/el/7/noarch/RPMS/mesosphere-el-
repo-7-3.noarch.rpm  
RUN yum install mesos-0.28.2 -y  
  
EXPOSE 12321  
WORKDIR "/opt/Cook"  
CMD ["/usr/bin/java", "-cp", "bin/cook-standalone.jar", "cook.components",
"etc/config.edn"]  

