#  
# 安装： docker build -t dante ./  
# 运行： docker run -d -p 8822:22 -p 1080:1080 dante  
#  
#安装本地Centos  
FROM scratch  
MAINTAINER The CentOS Project <cloud-ops@centos.org>  
ADD centos-7-docker.tar.xz /  
LABEL name="CentOS Base Image"  
LABEL vendor="CentOS"  
LABEL license=GPLv2  
CMD ["/bin/bash"]  
#安装openssh和unzip工具  
RUN rpm --rebuilddb  
RUN yum install unzip openssh-server -y  
#生成ssh的登陆证书  
RUN ssh-keygen -q -t rsa -b 2048 -f /etc/ssh/ssh_host_rsa_key -N ''  
RUN ssh-keygen -q -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N ''  
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_ed25519_key -N ''  
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key -N ''  
#修改ssh-server的配置  
RUN sed -i "s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g"
/etc/ssh/sshd_config  
RUN sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config  
#修改当前系统的ROOT密码  
RUN echo "root:root" > /tmp/tmp.pass  
RUN chpasswd < /tmp/tmp.pass  
#安装依赖包  
RUN rpm --rebuilddb  
RUN yum install gcc openssl-devel pcre-devel zlib-devel libtool c++ make -y  
#编译安装dante包,注意：tar.gz会自动解压  
ADD dante-1.4.2.tar.gz /opt/  
RUN cd /opt/dante-1.4.2 && ./configure && make && make install  
#增加可登陆的用户  
RUN useradd -s /sbin/nologin proxy  
RUN echo "proxy:proxy" > /tmp/proxy.pass  
RUN chpasswd < /tmp/proxy.pass  
ADD danted.conf /etc/danted.conf  
RUN echo "sockd -f /etc/danted.conf" > /opt/danted.sh  
#设置读写权限  
RUN chmod -R 777 /opt  
#设置进入启动项  
ENTRYPOINT /opt/danted.sh & /usr/sbin/sshd -D

