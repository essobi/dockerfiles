FROM jboss/torquebox  
USER root  
  
ADD http://mirror.centos.org/centos/7/os/x86_64/Packages/yum-plugin-
ovl-1.1.31-40.el7.noarch.rpm /root/yum-plugin-ovl-1.1.31-40.el7.noarch.rpm  
RUN rpm -ivh /root/yum-plugin-ovl-1.1.31-40.el7.noarch.rpm  
# And we continue.  
RUN yum -y update  
ADD https://s3.amazonaws.com/jruby.org/downloads/1.7.19/jruby-bin-1.7.19.zip
/root/jruby.zip  
WORKDIR /root  
  
RUN unzip jruby.zip && \  
mv /root/jruby-1.7.19/bin/* /usr/local/bin/ && \  
mv /root/jruby-1.7.19/lib/* /usr/local/lib/ && \  
rm -fr /root/jruby-1.7.19  
  
RUN rpm -ivh https://yum.puppetlabs.com/puppetlabs-release-pc1-el-7.noarch.rpm
&& \  
yum install -y puppet tar && yum clean all  
  
ADD start.sh /  
  
ENV HOSTNAME razor-server  
ENV TORQUEBOX_HOME /opt/razor-torquebox  
ENV JBOSS_HOME $TORQUEBOX_HOME/jboss  
ENV JRUBY_HOME $TORQUEBOX_HOME/jruby  
ENV PATH $JRUBY_HOME/bin:$PATH  
  
RUN yum install -y git && yum clean all && \  
gem install bundler  
  
RUN yum install -y wget libarchive-devel && yum clean all  
  
WORKDIR /opt  
  
ADD https://github.com/puppetlabs/razor-server/archive/1.5.0.zip
/opt/1.5.0.zip  
RUN unzip 1.5.0.zip && mv razor-server-1.5.0 razor-server && \  
cd razor-server  
  
# Overriding  
ADD config.yaml /opt/razor-server/config.yaml  
  
WORKDIR /opt/razor-server  
  
RUN bundle install && \  
mkdir -p /var/lib/razor/repo-store && \  
mkdir -p /scripts  
  
VOLUME /opt/custom-tasks  
  
ADD install_microkernel.sh /scripts/  
ADD deploy_razor.sh /scripts/  
  
RUN /scripts/install_microkernel.sh  
  
EXPOSE 8080  
RUN chmod +x /start.sh  
CMD ["/start.sh"]  

