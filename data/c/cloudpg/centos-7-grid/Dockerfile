FROM centos:7  
LABEL maintainer="mirco.tracolli@pg.infn.it"  
LABEL Version=1.0  
  
# Reference for EL7 Worker Node  
# wn metapackage: https://twiki.cern.ch/twiki/bin/view/LCG/EL7WNMiddleware  
# Update system and install wget  
RUN echo "LC_ALL=C" >> /etc/environment \  
&& echo "LANGUAGE=C" >> /etc/environment \  
&& yum --setopt=tsflags=nodocs -y update \  
&& yum --setopt=tsflags=nodocs -y install wget \  
&& yum clean all  
  
# Add yum repos  
WORKDIR /etc/pki/rpm-gpg  
RUN wget http://linuxsoft.cern.ch/wlcg/RPM-GPG-KEY-wlcg  
  
WORKDIR /etc/yum.repos.d  
RUN wget
http://repository.egi.eu/community/software/preview.repository/2.0/releases/repofiles/centos-7-x86_64.repo
\  
&& wget http://repository.egi.eu/sw/production/cas/1/current/repo-files/EGI-
trustanchors.repo \  
&& wget http://linuxsoft.cern.ch/wlcg/wlcg-centos7.repo  
  
# Add singularity  
RUN yum -y clean all --enablerepo=* \  
&& yum -y update \  
&& yum -y install singularity-runtime  
  
# Add grid stuff  
WORKDIR /root  
RUN yum --setopt=tsflags=nodocs -y install epel-release yum-plugin-ovl \  
&& yum --setopt=tsflags=nodocs -y install fetch-crl wn \  
&& yum clean all  

