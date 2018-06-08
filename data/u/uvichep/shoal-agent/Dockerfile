# shoal-agent  
#  
# VERSION 0.0.2  
FROM centos:6  
MAINTAINER Ian Gable <igable@uvic.ca>  
  
RUN yum update -y \  
&& yum install epel-release -y \  
&& curl http://shoal.heprc.uvic.ca/repo/shoaldev.repo -o
/etc/yum.repos.d/shoal.repo \  
&& yum update -y \  
&& rpm --import http://hepnetcanada.ca/pubkeys/igable.asc \  
&& yum install shoal-agent -y \  
&& yum clean all  
  
COPY ent /bin/  
  
ENTRYPOINT ["ent"]  

