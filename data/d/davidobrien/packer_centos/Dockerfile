From centos:latest  
  
RUN yum update -y  
RUN yum --enablerepo=extras install epel-release -y  
RUN yum group install -y "Development Tools"  
RUN yum -y install python2-pip  
RUN pip install --upgrade pip  
RUN pip install awscli  
RUN pip install boto  
# Change this URL to the exact version you want to install  
ENV POWERSHELL_DOWNLOAD_URL
https://github.com/PowerShell/PowerShell/releases/download/v6.0.0-beta.9/powershell-6.0.0_beta.9-1.rhel.7.x86_64.rpm  
  
RUN curl -L $POWERSHELL_DOWNLOAD_URL \--output powershell_linux.rpm  
RUN yum -y install powershell_linux.rpm  
RUN rm powershell_linux.rpm --force  
RUN pwsh -command "Install-Module -Name AwsPowerShell.NetCore -Force -Verbose"  
  
RUN curl -O
https://releases.hashicorp.com/packer/1.1.1/packer_1.1.1_linux_amd64.zip  
RUN unzip packer_1.1.1_linux_amd64.zip  
RUN cp packer /usr/local/bin/packer  
RUN rm packer  
RUN packer --version  
RUN yum clean packages  
RUN yum clean all

