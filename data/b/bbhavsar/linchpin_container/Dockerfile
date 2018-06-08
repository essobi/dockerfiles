FROM fedora  
MAINTAINER Bhavik Bhavsar (9.bhavik@gmail.com)  
RUN dnf install -y rpm rpm-build python-pip gcc wget git libffi-devel redhat-
rpm-config python-devel\  
openssl-devel && dnf clean all  
RUN ssh-keygen -f /root/.ssh/id_rsa -t rsa -N ''  
RUN printf "Host *\n StrictHostKeyChecking no" > /root/.ssh/config  
RUN wget https://copr-
be.cloud.fedoraproject.org/results/@pki/10.5/epel-7-x86_64/00760967-test-pki-
modules/test-pki-modules-0.1-1.noarch.rpm --no-check-certificate  
RUN rpm -ivh test-pki-modules-0.1-1.noarch.rpm  
RUN pip install linchpin==1.0.2  
RUN pip install ansible==2.3.2 pytest-ansible==1.3.1 pytest-ansible-
playbook==0.3.0 pytest-logger pytest-autochecklog==0.2.0 pexpect  

