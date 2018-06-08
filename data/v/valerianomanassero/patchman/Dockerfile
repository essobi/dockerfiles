FROM centos:7  
MAINTAINER Valeriano Manassero https://github.com/valeriano-manassero  
  
ENV PATCHMAN_VERSION 1.7.0-2  
RUN yum -y update \  
&& yum -y install wget \  
&& yum clean all  
  
RUN wget https://download.patchman.co/repo/rhel/RPM-GPG-KEY-Patchman -O
/etc/pki/rpm-gpg/RPM-GPG-KEY-Patchman  
RUN wget https://download.patchman.co/repo/rhel/patchman.repo -O
/etc/yum.repos.d/patchman.repo  
RUN yum -y install patchman-client-${PATCHMAN_VERSION}.el7.centos  
  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
CMD ["/docker-entrypoint.sh"]

