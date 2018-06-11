FROM centos:7.4.1708  
RUN curl -sSL https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-
init_1.1.3_amd64 -o /usr/local/bin/dumb-init  
RUN chmod +x /usr/local/bin/dumb-init  
  
RUN yum -y install wget  
RUN rm -rf /etc/yum.repos.d/*  
RUN wget -O /etc/yum.repos.d/CentOS-Base.repo
http://mirrors.aliyun.com/repo/Centos-7.repo  
RUN wget -O /etc/yum.repos.d/epel.repo
http://mirrors.aliyun.com/repo/epel-7.repo  
  
RUN rm -rf /var/cache/yum/  

