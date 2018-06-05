FROM ubuntu:xenial  
RUN echo "===> Adding Ansible's PPA..." && \  
echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu xenial main" | tee
/etc/apt/sources.list.d/ansible.list && \  
echo "deb-src http://ppa.launchpad.net/ansible/ansible/ubuntu xenial main" |
tee -a /etc/apt/sources.list.d/ansible.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 7BB9C367 &&
\  
DEBIAN_FRONTEND=noninteractive apt-get update && \  
echo "===> Installing Ansible..." && \  
apt-get install -y ansible=2.4.3.0-1ppa~xenial && \  
echo "===> Removing Ansible PPA..." && \  
rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/ansible.list  
RUN apt-get update && apt-get install -y --no-install-recommends python-pip
git unzip  
RUN pip install boto3 botocore  
RUN pip install awscli==1.14.39  
  
ADD https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64
/usr/local/bin/jq  
ADD https://releases.hashicorp.com/packer/1.1.2/packer_1.1.2_linux_amd64.zip
/root/packer.zip  
ADD
https://releases.hashicorp.com/terraform/0.11.3/terraform_0.11.3_linux_amd64.zip
/root/terraform.zip  
ADD aws-ebs-traveloka-ansible.json /root/  
  
RUN unzip /root/packer.zip -d /usr/local/bin  
RUN unzip /root/terraform.zip -d /usr/local/bin  
RUN chmod +x /usr/local/bin/jq  

