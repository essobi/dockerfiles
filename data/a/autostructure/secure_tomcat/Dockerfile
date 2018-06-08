FROM centos:latest  
  
ENV PUPPET_AGENT_VERSION="1.8.1" R10K_VERSION="2.2.2"  
WORKDIR /  
  
RUN rpm -Uvh https://yum.puppetlabs.com/puppetlabs-release-pc1-el-7.noarch.rpm
&& \  
yum upgrade -y && \  
yum update -y && \  
yum install -y puppet-agent-"$PUPPET_AGENT_VERSION" && \  
yum clean all  
  
RUN yum update -y && \  
yum install -y git && \  
/opt/puppetlabs/puppet/bin/gem install r10k:"$R10K_VERSION" \--no-ri --no-rdoc
&& \  
yum clean all  
  
COPY Puppetfile /Puppetfile  
RUN /opt/puppetlabs/puppet/bin/r10k puppetfile install --moduledir
/etc/puppetlabs/code/modules  
  
COPY manifests /manifests  
  
RUN yum update -y && \  
FACTER_hostname=secure_tomcat /opt/puppetlabs/bin/puppet apply
manifests/init.pp --verbose --show_diff --summarize --app_management && \  
yum clean all  
  
LABEL com.puppet.inventory="/inventory.json"  
RUN /opt/puppetlabs/bin/puppet module install puppetlabs-inventory && \  
/opt/puppetlabs/bin/puppet inventory all > /inventory.json  
  
EXPOSE 8080  
USER tomcat_admin  
  
CMD ["/usr/local/tomcat/bin/catalina.sh", "run"]  

