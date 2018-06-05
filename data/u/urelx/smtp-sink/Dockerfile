# smtp-sink  
#  
# VERSION 0.0.1  
FROM centos  
MAINTAINER Yuu Yamanaka <yuu@relx.jp>  
  
RUN yum install -y postfix  
  
EXPOSE 25  
CMD ["smtp-sink", "-u", "postfix", "0.0.0.0:25", "100"]  

