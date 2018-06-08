FROM centos  
  
MAINTAINER P Pavlov "ppavlov@nomail.com"  
# yum update  
RUN yum update -y  
  
#RUN setenforce 0  
#RUN sed -i 's/SELINUX=enforcing/SELINUX=permissive/g' /etc/selinux/config  
#RUN sed -i 's#localhost#foreman.sainsburys.co.uk foreman#' /etc/hosts  
RUN echo "127.0.0.1 foreman.sainsburys.co.uk foreman" >> /etc/hosts  
  
# install the katello-repos  
RUN yum -y localinstall
http://fedorapeople.org/groups/katello/releases/yum/3.2/katello/el7/x86_64/katello-
repos-latest.rpm  
RUN yum -y localinstall
http://yum.theforeman.org/releases/nightly/el7/x86_64/foreman-release.rpm  
RUN yum -y localinstall http://yum.puppetlabs.com/puppetlabs-release-
el-7.noarch.rpm  
RUN yum -y localinstall http://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN yum -y install foreman-release-scl  
  
# install katello  
RUN yum -y install katello  
  
#Adding the Configuration files  
ADD run.sh /run.sh  
ADD foreman-answers.yaml /etc/foreman-installer/scenarios.d/foreman-
answers.yaml  
ADD katello-answers.yaml /etc/foreman-installer/scenarios.d/katello-
answers.yaml  
ADD capsule-answers.yaml /etc/foreman-installer/scenarios.d/capsule-
answers.yaml  
  
### ports  
# puppet (via apache)  
EXPOSE 8140  
# foreman-proxy  
EXPOSE 8443  
# foreman (via apache) and provisioning purposes  
EXPOSE 80  
# api communication  
EXPOSE 443  
EXPOSE 8080  
# qpid ssl  
EXPOSE 5671  
# smart proxy  
EXPOSE 9090  
CMD ["/run.sh"]  

