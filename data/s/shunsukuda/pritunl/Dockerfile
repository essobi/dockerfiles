FROM centos  
MAINTAINER Shunsuke Tsukuda  
  
RUN yum -y install epel-release  
COPY ./mongodb-org-3.2.repo /etc/yum.repos.d/mongodb-org-3.2.repo  
COPY ./pritunl.repo /etc/yum.repos.d/pritunl.repo  
RUN gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys
7568D9BB55FF9E5287D586017AE645C0CF8E292A  
RUN gpg --armor --export 7568D9BB55FF9E5287D586017AE645C0CF8E292A > key.tmp  
RUN rpm --import key.tmp  
RUN rm -f key.tmp  
RUN yum -y install pritunl mongodb-org  
  
EXPOSE 9700  
VOLUME /var/docker/pritunl  
COPY ./pritunl.conf /etc/pritunl.conf  
CMD pritunl start  

