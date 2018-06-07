FROM centos  
MAINTAINER Ramesh B  
  
ENV USER_HOME /home/cloud-user  
ARG user=cloud-user  
ARG group=cloud-user  
ARG uid=1000  
ARG gid=1000  
RUN sed -i '/tsflags/s/^/#/g' /etc/yum.conf  
  
RUN yum -y update \  
&& yum -y install perl \  
&& yum -y install java \  
&& yum -y install python \  
&& yum -y install less \  
&& yum -y install sudo \  
&& yum -y install vim-enhanced \  
&& yum -y install nano \  
&& yum -y install man \  
&& yum -y install man-pages  
  
RUN groupadd -g ${gid} ${group} \  
&& useradd -u ${uid} -g ${gid} -m -s /bin/bash ${user}  
  
VOLUME /home/cloud-user  
  
RUN echo "cloud-user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/cloud-user  
  
USER ${user}  
  
CMD ["/bin/bash"]  

