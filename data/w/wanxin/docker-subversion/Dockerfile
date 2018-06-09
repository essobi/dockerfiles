FROM centos:6.7  
MAINTAINER wanxin <258621580@qq.com>  
  
#svn repository dir(in container)  
ENV REPO_DIR /opt/svn/repo  
  
# Install Subversion  
RUN yum install -y subversion && \  
yum clean all  
  
# Copy init config and script  
COPY config /opt/svn/config  
COPY script /opt/svn/script  
RUN chmod +x /opt/svn/script/run.sh  
  
EXPOSE 3690  
  
ENTRYPOINT ["/opt/svn/script/run.sh"]

