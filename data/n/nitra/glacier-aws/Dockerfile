FROM ubuntu:16.04  
MAINTAINER Vladislav Stetsenko <v.stecenko@nitralabs.com>  
  
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
  
#clone work glacier project and set workdir with start python setup  
RUN git clone https://github.com/uskudnik/amazon-glacier-cmd-interface.git  
WORKDIR amazon-glacier-cmd-interface  
RUN python setup.py install  
RUN mkdir /root/.aws  
COPY credentials /root/.aws/  
COPY config /root/.aws/  
#######################################  
#RUN mkdir /root/script/  
RUN mkdir /folder  
COPY script /amazon-glacier-cmd-interface/script  
RUN chmod u+x /amazon-glacier-cmd-interface/script/*  
RUN chmod 777 /amazon-glacier-cmd-interface/script/*  
RUN chmod 755 /etc/crontab  
RUN touch /var/log/cron.log  
CMD ["cron", "-f"]  

