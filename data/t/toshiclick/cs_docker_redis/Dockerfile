FROM centos:latest  
  
# 作成者情報  
MAINTAINER toshi <toshi@toshi.click>  
  
# yum update  
RUN yum -y update && yum clean all  
  
# set locale  
RUN yum -y update && yum reinstall -y glibc-common && yum clean all  
RUN yum -y update && yum install -y vim kbd ibus-kkc vlgothic-* && yum clean
all  
RUN localedef -f UTF-8 -i ja_JP ja_JP.UTF-8  
ENV LANG ja_JP.UTF-8  
ENV LANGUAGE ja_JP:ja  
ENV LC_ALL ja_JP.UTF-8  
RUN unlink /etc/localtime  
RUN ln -s /usr/share/zoneinfo/Japan /etc/localtime  
  
#-----------------------------------------------------------------------------------------------------  
# ↑までは共通  
#-----------------------------------------------------------------------------------------------------  
# yum install redis  
RUN yum -y update && yum -y install epel-release && yum -y install redis &&
yum clean all  
  
ADD redis.conf /etc/redis.conf  
  
CMD ["redis-server", "/etc/redis.conf"]  
  
# Dockerコンテナの指定したポートを開き他から参照できるようにします。  
EXPOSE 6379  

