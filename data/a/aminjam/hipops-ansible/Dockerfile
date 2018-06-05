FROM debian:stable  
MAINTAINER Amin Jams <aminjam@outlook.com>  
  
RUN apt-get update  
RUN apt-get install -y python-pip python-dev python-crypto git wget unzip
--fix-missing  
RUN yes w | pip install paramiko PyYAML Jinja2 httplib2 boto ansible==1.7.2  
ENV ANSIBLE_HOST_KEY_CHECKING False  
  
##hipops installation  
RUN wget -q --no-check-certificate
https://github.com/aminjam/hipops/releases/download/0.1.2/hipops-linux-amd64
-O /usr/bin/hipops  
RUN chmod u+x /usr/bin/hipops  
  
#hipops-ansible default playbooks  
RUN wget -q --no-check-certificate https://github.com/aminjam/hipops-
playbooks/archive/ansible.zip && \  
unzip ansible.zip && mv -f ./hipops-playbooks-ansible /home && \  
rm ansible.zip  
ENV PLAYBOOK_PATH /home/hipops-playbooks-ansible/ansible  
  
#configure ansible for aws  
RUN mkdir -p /etc/ansible  
RUN wget -q --no-check-certificate
https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.py
-O /etc/ansible/hosts  
RUN wget -q --no-check-certificate
https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.ini
-O /etc/ansible/ec2.ini  
RUN chmod +x /etc/ansible/hosts  
  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
##################### INSTALLATION END #####################  
RUN echo `hipops -v` `ansible --version`  
WORKDIR /home/app  
ENTRYPOINT ["/run.sh"]  
CMD []  

