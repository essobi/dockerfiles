FROM python:2.7-jessie  
RUN apt-get update && \  
apt-get -y install sudo unzip  
RUN wget -P /tmp
https://releases.hashicorp.com/terraform/0.10.7/terraform_0.10.7_linux_amd64.zip
&& \  
unzip /tmp/terraform_0.10.7_linux_amd64.zip && \  
chmod +x terraform && \  
mv terraform /usr/local/bin && \  
ln -s /usr/local/bin/terraform /usr/local/bin/terraform_v0.10.7  
ADD iac-requirements.txt /cm/requirements.txt  
ADD run_terraform_apply.sh /run_terraform_apply.sh  
ADD run_terraform_destroy.sh /run_terraform_destroy.sh  
ADD run_unregister_nodes.sh /run_unregister_nodes.sh  
ADD create_cluster.sh /create_cluster.sh  
  
WORKDIR /cm  
RUN addgroup --system --gid 981 herbie_bot && \  
adduser --system --uid 981 --gid 981 --home /home/herbie_bot herbie_bot  
RUN echo "herbie_bot ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/herbie_bot && \  
chmod 0440 /etc/sudoers.d/herbie_bot  
  
USER herbie_bot  
WORKDIR /home/herbie_bot  
RUN mkdir /home/herbie_bot/.aws  
RUN sudo pip install -r /cm/requirements.txt  

