FROM centos:latest  
  
MAINTAINER Ivan Subotic <ivan.subotic@unibas.ch>  
  
RUN yum -y update && \  
yum -y install perl perl-core && \  
yum clean all  
  
RUN rpm -Uvh
http://franz.com/ftp/pri/acl/ag/ag6.3.0/linuxamd64.64/agraph-6.3.0-1.x86_64.rpm  
  
RUN /usr/bin/configure-agraph \  
\--non-interactive \  
\--runas-user agraph \  
\--create-runas-user \  
\--super-user test \  
\--super-password xyzzy  
  
RUN mkdir -p /var/run/agraph /var/lib/agraph/settings /var/log/agraph  
RUN chown -R agraph:agraph /var/run/agraph /var/lib/agraph /var/log/agraph  
  
EXPOSE 10035  
VOLUME ["/var/lib/agraph"]  
  
CMD ["/usr/bin/agraph", "--no-daemonize"]

