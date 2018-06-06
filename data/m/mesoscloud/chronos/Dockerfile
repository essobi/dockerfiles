FROM centos:7  
MAINTAINER Peter Ericson <pdericson@gmail.com>  
  
# https://github.com/Yelp/dumb-init  
RUN curl -fLsS -o /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.0.2/dumb-init_1.0.2_amd64 && chmod +x
/usr/local/bin/dumb-init  
  
RUN rpm -i http://repos.mesosphere.io/el/7/noarch/RPMS/mesosphere-el-
repo-7-1.noarch.rpm && \  
yum -y install chronos-2.4.0 mesos-0.24.1  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/usr/local/bin/dumb-init", "/entrypoint.sh"]  

