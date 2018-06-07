FROM centos:7  
LABEL maintainer "it@eltiempo.es"  
LABEL version "1.0"  
LABEL description "Image with sphinx search server"  
ENV container docker  
  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm && \  
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm && \  
yum -y --setopt=tsflags=nodocs update && \  
yum -y --setopt=tsflags=nodocs install epel-release && \  
yum -y --setopt=tsflags=nodocs install net-tools vim wget curl && \  
yum -y --setopt=tsflags=nodocs install postgresql-libs unixODBC && \  
yum clean all  
  
RUN wget http://sphinxsearch.com/files/sphinx-2.2.11-1.rhel7.x86_64.rpm && \  
yum -y --setopt=tsflags=nodocs install sphinx-2.2.11-1.rhel7.x86_64.rpm && \  
yum clean all  
  
RUN mkdir -p /var/run/sphinx && \  
mkdir -p /var/sphinx/idx && \  
chown -R sphinx.sphinx /var/run/sphinx && \  
chown -R sphinx.sphinx /var/sphinx/idx && \  
ln -s /dev/stdout /var/log/sphinx/query.log && \  
ln -s /dev/stdout /var/log/sphinx/searchd.log  
  
RUN yum -y --setopt=tsflags=nodocs install mariadb && \  
yum clean all  
  
COPY startup.sh /usr/local/bin/startup.sh  
RUN chmod -v +x /usr/local/bin/startup.sh  
  
EXPOSE 9306 9312  
CMD ["/usr/local/bin/startup.sh"]

