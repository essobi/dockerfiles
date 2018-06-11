FROM centos:6  
MAINTAINER Tsubasa YUMURA @yumu19  
RUN yum -y update  
RUN yum -y install mercurial which  
RUN cd /tmp && hg clone https://bitbucket.org/okamototk/kanonconductor  
RUN yes | /tmp/kanonconductor/kanon-setup  
RUN echo 'export PATH=/opt/kanon/bin/:$PATH' >> /root/.bash_profile  
RUN source /root/.bash_profile  

