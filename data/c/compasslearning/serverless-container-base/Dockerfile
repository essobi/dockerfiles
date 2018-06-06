FROM atlassian/default-image:latest  
  
# Get the latest Ansible  
RUN apt-get install software-properties-common  
RUN apt-add-repository ppa:ansible/ansible  
  
# Update installed libs  
RUN apt-get update -q  
  
# Install ZIP  
RUN apt-get install -y zip  
  
# Remove any installed nodejs and install 6.x from Node  
RUN apt-get purge nodejs npm  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get install -y nodejs  
  
# Workaround required for serverless install bug introduced in 1.15.1  
RUN npm config set unsafe-perm=true  
  
# Install SERVERLESS  
RUN npm install -g serverless  
  
# Install ANSIBLE  
RUN apt-get install -y ansible  
  
# Install python-pip  
RUN apt-get install -y python-pip  
  
# Install boto and boto3  
RUN pip install boto  
RUN pip install boto3  
  
# Install aws cli  
RUN pip install --upgrade awscli  
  
# -- Install .NET --  
# Register the trusted Microsoft signature key  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >
microsoft.gpg  
RUN mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg  
  
# Register the Microsoft Product feed for Ubuntu 14.04  
RUN sh -c 'echo "deb [arch=amd64]
https://packages.microsoft.com/repos/microsoft-ubuntu-trusty-prod trusty main"
> /etc/apt/sources.list.d/dotnetdev.list'  
  
# Install the .NET Core SDK  
RUN apt-get update  
RUN apt-get install -y dotnet-sdk-2.0.0

