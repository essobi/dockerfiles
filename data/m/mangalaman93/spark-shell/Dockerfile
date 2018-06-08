FROM mangalaman93/spark:2.1.0  
MAINTAINER Aman Mangal <mangalaman93@gmail.com>  
  
# explicitly set user/group IDs  
RUN groupadd -r hadoop --gid=1000 && useradd -r -g hadoop -d /home/hadoop
--uid=1000 hadoop  
  
# We need mesosphere libs for running spark with mesos  
RUN rpm -Uvh http://repos.mesosphere.com/el/7/noarch/RPMS/mesosphere-el-
repo-7-1.noarch.rpm && \  
yum -y install mesos && \  
yum clean all  
  
RUN mkdir -p /home/hadoop && \  
chown -R hadoop:hadoop /home/hadoop  
  
WORKDIR /home/hadoop  
USER hadoop  
ENTRYPOINT [ "/opt/spark/bin/spark-shell" ]  

