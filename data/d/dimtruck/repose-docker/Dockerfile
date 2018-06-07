FROM centos:7  
MAINTAINER Dimitry Ushakov <dimitry.ushakov@rackspace.com>  
  
RUN yum update -y && yum install -y wget  
RUN wget http://pkgs.repoforge.org/rpmforge-release/rpmforge-
release-0.5.3-1.el7.rf.x86_64.rpm  
RUN rpm -Uvh rpmforge-release-0.5.3-1.el7.rf.x86_64.rpm  
RUN wget -O /etc/yum.repos.d/openrepose.repo
http://repo.openrepose.org/el/openrepose.repo  
  
RUN wget
http://mirrors.karan.org/epel7/Packages/daemonize/20131231020837/1.7.3-1.el6.x86_64/daemonize-1.7.3-1.el7.x86_64.rpm  
RUN rpm -Uvh daemonize-1.7.3-1.el7.x86_64.rpm  
  
RUN yum update -y && yum install -y repose-valve-7.3.0.0 repose-filter-
bundle-7.3.0.0 repose-extensions-filter-bundle-7.3.0.0  
  
VOLUME /etc/repose  
WORKDIR /etc/repose  
USER repose  
  
EXPOSE 8080 9777  
CMD java -Xmx512M -Xms512M -XX:+HeapDumpOnOutOfMemoryError
-XX:HeapDumpPath=/tmp/dump-repose.hprof -XX:MaxPermSize=128M -jar
/usr/share/repose/repose-valve.jar -c /etc/repose  
  

