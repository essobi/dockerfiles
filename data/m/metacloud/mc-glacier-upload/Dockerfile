FROM ubuntu:16.04  
MAINTAINER David Pippenger <riven@particle-man.com>  
  
# install git and pip  
RUN apt-get update && apt-get install -y python-pip git \  
awscli/xenial\  
wget\  
vim\  
cron \  
ssmtp\  
mailutils\  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Pull specific version of glacier-cmd-interface from hash committed on Sept
1st 2016.  
RUN git clone https://github.com/uskudnik/amazon-glacier-cmd-interface.git \  
&& cd amazon-glacier-cmd-interface \  
&& git checkout 9f28132f9872e1aad9e956e5613b976504e930c8 \  
&& python setup.py install  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod 755 /usr/local/bin/entrypoint.sh  
  
ENV VAULT_NAME=""  
ENV UPLOAD_DIR="/upload"  
ENV aws_access_key=""  
ENV aws_secret_key=""  
ENV region=""  
ENV bookkeeping="False"  
ENV bookkeeping-domain-name=""  
ENTRYPOINT ["entrypoint.sh"]  

