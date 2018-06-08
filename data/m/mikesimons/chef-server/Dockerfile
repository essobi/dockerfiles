FROM centos:6  
RUN curl -s
https://packagecloud.io/install/repositories/chef/stable/script.rpm.sh | bash  
RUN yum install -y chef-server-core opscode-manage && yum clean all  
RUN yum install -y vixie-cron crontabs && yum clean all  
RUN ln -sf /bin/true /sbin/initctl  
  
ADD ./run.sh /run.sh  
CMD ["/run.sh"]  
  
EXPOSE 443  
VOLUME ["/chef-setup"]  
  

