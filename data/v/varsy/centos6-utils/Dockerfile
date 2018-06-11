FROM sergeyzh/centos6-epel  
  
MAINTAINER Sergey Zhukov, sergey@jetbrains.com; Andrey Sizov,
andrey.sizov@jetbrains.com  
  
# Setup base packages  
RUN yum install -y \  
openssh-clients \  
git \  
unzip \  
sendmail \  
mailx \  
mysql \  
telnet \  
openssl \  
which \  
python-pip \  
iftop \  
postgresql  
  
# Setup awscli  
RUN pip install \  
awscli  
  
CMD /bin/bash  

