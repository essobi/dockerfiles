#  
# Create a docker image suitable for day to day use when on client  
# sites rather than pollute the OSX Base OS on my laptop.  
# Yes this is pretty heavy for a container....  
#  
FROM centos:7  
MAINTAINER Keiran Sweet "Keiran@gmail.com"  
RUN yum -y update  
RUN yum -y install epel-release  
RUN yum -y install which git vim mlocate curl sudo unzip file python-devel
python-pip python34 python34-devel wget bind-utils  
RUN useradd -m -u 501 keiran  
RUN chown keiran:keiran /home/keiran/  
RUN echo '%wheel ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/wheel  
RUN chmod 0440 /etc/sudoers.d/wheel  
  
# Install RVM and a copy of Ruby 2.3  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN curl -sSL https://get.rvm.io | bash -s stable  
RUN usermod -G rvm,wheel keiran  
RUN usermod -G rvm root  
RUN su - root -c "rvm install 2.3"  
  
# Install the AWS CLI Tools  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o
"/var/tmp/awscli-bundle.zip"  
WORKDIR /var/tmp/  
RUN unzip awscli-bundle.zip  
WORKDIR /var/tmp/awscli-bundle/  
RUN /var/tmp/awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
RUN rm -f /var/tmp/awscli-bundle.zip  
RUN rm -rf /var/tmp/awscli-bundle  
  
# Install Powershell  
RUN yum -y install
https://github.com/PowerShell/PowerShell/releases/download/v6.0.0-beta.2/powershell-6.0.0_beta.2-1.el7.x86_64.rpm  
  
# Install Puppet Enterprise and the Gems for Azure.  
RUN yum --nogpgcheck install -y https://pm.puppetlabs.com/puppet-
agent/2017.2.1/1.10.1/repos/el/7/PC1/x86_64/puppet-
agent-1.10.1-1.el7.x86_64.rpm  
RUN /opt/puppetlabs/puppet/bin/gem install retries --no-ri --no-rdoc  
RUN /opt/puppetlabs/puppet/bin/gem install azure --version='~>0.7.0' \--no-ri
--no-rdoc  
RUN /opt/puppetlabs/puppet/bin/gem install azure_mgmt_compute
--version='~>0.3.0' \--no-ri --no-rdoc  
RUN /opt/puppetlabs/puppet/bin/gem install azure_mgmt_storage
--version='~>0.3.0' \--no-ri --no-rdoc  
RUN /opt/puppetlabs/puppet/bin/gem install azure_mgmt_resources
--version='~>0.3.0' \--no-ri --no-rdoc  
RUN /opt/puppetlabs/puppet/bin/gem install azure_mgmt_network
--version='~>0.3.0' \--no-ri --no-rdoc  
RUN /opt/puppetlabs/puppet/bin/gem install hocon --version='~>1.1.2' \--no-ri
--no-rdoc  
  
# Install the latest Puppet Development Kit (PDK)  
RUN yum --nogpgcheck install -y https://puppet-
pdk.s3.amazonaws.com/pdk/1.0.1.0/repos/el/7/PC1/x86_64/pdk-1.0.1.0-1.el7.x86_64.rpm  
  
# Install the Azure CLI  
WORKDIR /var/tmp/  
RUN curl -O https://bootstrap.pypa.io/get-pip.py  
RUN /usr/bin/python3 get-pip.py  
RUN /usr/bin/pip3 install azure-cli  
RUN rm -f /bin/python  
RUN ln -s /bin/python3 /bin/python  
  
# Install JQ  
WORKDIR /usr/local/bin/  
RUN wget https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64  
RUN mv jq-linux64 jq  
RUN chmod 755 /usr/local/bin/jq  
  
WORKDIR /  
  
CMD ["/bin/bash"]  
  

