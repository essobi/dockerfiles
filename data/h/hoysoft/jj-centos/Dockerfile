FROM centos:7.3.1611  
MAINTAINER Justin.h<justin@5nas.cc>  
  
#修改容器时区  
RUN rm -rf /etc/localtime  
RUN ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
#安装SSHD  
RUN yum install -y openssh-server sudo  
RUN sed -i 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config  
#安装openssh-clients  
RUN yum install -y openssh-clients \  
&& rm -rf /var/cache/yum/*  
  
# ENV SSH_ROOT_PASSWORD="root"  
# 添加用户root，密码root，并且将此用户添加到sudoers里  
# RUN echo "root:${SSH_ROOT_PASSWORD}" | chpasswd  
# RUN echo "root ALL=(ALL) ALL" >> /etc/sudoers  
# 下面这两句比较特殊，在centos6上必须要有，否则创建出来的容器sshd不能登录  
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key  
  
RUN mkdir /var/run/sshd  
  
# VOLUME /var/lib/mysql  
COPY docker-entrypoint.sh /ssh-entrypoint.sh  
RUN chmod -v +x /ssh-entrypoint.sh  
ENTRYPOINT ["/ssh-entrypoint.sh"]  
  
# COPY centos-ssh-start.sh /centos-ssh-start.sh  
# RUN chmod -v +x /centos-ssh-start.sh  
# 启动sshd服务并且暴露22端口  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  
#CMD ["/centos-ssh-start.sh"]  

