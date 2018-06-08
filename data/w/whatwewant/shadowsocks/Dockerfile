# 拉取镜像  
FROM ubuntu:14.04  
  
# 维护者信息  
MAINTAINER Cole Smith <tobewhatwewant@gmail.com>  
  
# backup old sources.list  
RUN cp /etc/apt/sources.list /etc/apt/sources.list.bac  
COPY sources.list /etc/apt/sources.list  
COPY resolv.conf /etc/resolv.conf  
  
# 更换为163的源，国内你懂的  
# RUN echo "deb http://mirrors.163.com/ubuntu/ trusty main restricted universe
multiverse" > /etc/apt/sources.list && \  
# echo "deb http://mirrors.163.com/ubuntu/ trusty-security main restricte
universe multiverse" >> /etc/apt/sources.list && \  
# echo "deb http://mirrors.163.com/ubuntu/ trusty-updates main restricted
universe multiverse" >> /etc/apt/sources.list && \  
# echo "deb http://mirrors.163.com/ubuntu/ trusty-proposed main restricted
universe multiverse" >> /etc/apt/sources.list && \  
# echo "deb http://mirrors.163.com/ubuntu/ trusty-backports main restricted
universe multiverse" >> /etc/apt/sources.list && \  
# echo "deb-src http://mirrors.163.com/ubuntu/ trusty main restricted universe
multiverse" >> /etc/apt/sources.list && \  
# echo "deb-src http://mirrors.163.com/ubuntu/ trusty-security main restricted
universe multiverse" >> /etc/apt/sources.list && \  
# echo "deb-src http://mirrors.163.com/ubuntu/ trusty-updates main restricted
universe multiverse" >> /etc/apt/sources.list && \  
# echo "deb-src http://mirrors.163.com/ubuntu/ trusty-proposed main restricted
universe multiverse" >> /etc/apt/sources.list && \  
# echo "deb-src http://mirrors.163.com/ubuntu/ trusty-backports main
restricted universe multiverse" >> /etc/apt/sources.list  
  
# 更新源  
RUN apt-get -qqy update  
  
# 安装软件  
# 安装ssh  
# RUN apt-get install -qqy openssh-server  
  
# install shadowsocks  
COPY install_shadowsocks_libev.sh /tmp/install_shadowsocks_libev.sh  
RUN /bin/bash /tmp/install_shadowsocks_libev.sh  
COPY shadowsocks.json /etc/shadowsocks/shadowsocks.json  
COPY shadowsocks_1.json /etc/shadowsocks/shadowsocks_1.json  
COPY shadowsocks_2.json /etc/shadowsocks/shadowsocks_2.json  
COPY shadowsocks_3.json /etc/shadowsocks/shadowsocks_3.json  
COPY shadowsocks_4.json /etc/shadowsocks/shadowsocks_4.json  
COPY shadowsocks_5.json /etc/shadowsocks/shadowsocks_5.json  
RUN rm -rf /tmp/install_shadowsocks_libev.sh  
  
# 安装supervisor  
RUN apt-get install -qqy supervisor  
  
# 清理  
RUN apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
# 创建用户 ubuntu, 密码ubuntu  
# RUN export PASS=ubuntu && id -u ubuntu >>/dev/null 2>&1 || useradd --create-
home --shell /bin/bash --user-group --groups adm,sudo ubuntu && echo
"ubuntu:$PASS" | chpasswd  
  
# 复制supervisord配置  
# 确保当前目录有 supervisord.conf 文件  
# 配置写法，看下边  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# 指定主机数据卷(文件夹等)在容器中挂载  
# 和 -v HOST_DIR:CONTAINER_DIR 效果一致  
# 这里，将主机的/data目录挂载到容器/data, 容器会自动创建/data  
# VOLUME ["/etc"]  
  
# 映射端口  
# EXPOSE 22  
EXPOSE 10800  
# EXPOSE 11001  
EXPOSE 10801 10802 10803 10804 10805  
  
# 执行命令  
CMD ["/usr/bin/supervisord"]  
  
# 最后，终端创建, 命令如下  
# sudo docker build -t whatwewant/ubuntu:14.04 --no-cache --rm .  

