FROM centos:7  
RUN yum -y update  
  
# install inspec  
# https://docs.chef.io/packages.html  
RUN rpm --import https://packages.chef.io/chef.asc  
RUN sh -c 'echo -e "[chef-stable]\nname=chef-
stable\nbaseurl=https://packages.chef.io/repos/yum/stable/el/7/\$basearch/\ngpgcheck=1\nenabled=1\n"
>> /etc/yum.repos.d/chef-stable.repo'  
RUN yum install -y inspec  
  
# install azure cli  
RUN rpm --import https://packages.microsoft.com/keys/microsoft.asc  
RUN sh -c 'echo -e "[azure-cli]\nname=Azure
CLI\nbaseurl=https://packages.microsoft.com/yumrepos/azure-
cli\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc"
> /etc/yum.repos.d/azure-cli.repo'  
RUN yum install -y azure-cli  
  
# install terraform  
RUN yum install -y zip unzip wget  
RUN wget
https://releases.hashicorp.com/terraform/0.11.5/terraform_0.11.5_linux_amd64.zip
-O /usr/local/bin/terraform.zip  
RUN cd /usr/local/bin/ && unzip /usr/local/bin/terraform.zip  
RUN rm -f /usr/local/bin/terraform.zip  
RUN terraform --version  
  
# Install AWS CLI  
RUN curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py
| python  
RUN pip install awscli --upgrade --user  
ENV PATH="~/.local/bin:${PATH}"  
# Install VIM  
RUN yum install -y vim  

