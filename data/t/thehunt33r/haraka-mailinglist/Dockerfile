FROM centos:7  
MAINTAINER Matthieu ANTOINE "matthieuinspain+dockerhub@gmail.com"  
RUN yum -y update && yum -y upgrade && \  
yum -y install spamassassin git curl wget  
RUN curl -sL https://rpm.nodesource.com/setup | bash -  
RUN yum install -y nodejs gcc-c++ make  
RUN npm install -g Haraka  
RUN haraka -i /app  
COPY files/plugins /app/config/plugins  
COPY files/rcpt_to.alias_forward.js /app/plugins/rcpt_to.alias_forward.js  
COPY files/rcpt_to.alias_forward /app/config/rcpt_to.alias_forward  
EXPOSE 25  
CMD ["haraka", "-c", "/app/"]  

