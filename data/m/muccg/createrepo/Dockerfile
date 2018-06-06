#  
FROM muccg/rpmbuild:centos6  
MAINTAINER https://github.com/muccg  
  
RUN yum install -y \  
procmail \  
python27 \  
python27-pip \  
&& yum clean all  
  
RUN pip2.7 install -U pip \  
&& pip2.7 install awscli  
  
VOLUME ["/data"]  
  
COPY repos.txt /repos.txt  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
# Drop privileges, set home for ccg-user  
USER ccg-user  
ENV HOME /data  
WORKDIR /data  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/bin/sh"]  

