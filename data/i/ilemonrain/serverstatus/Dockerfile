FROM centos  
  
LABEL MAINTAINER ilemonrain <ilemonrain@ilemonrain.com>  
  
# 系统核心升级  
RUN ( yum update -y;\  
yum clean all ;\  
rm -rf /var/cache/yum )  
  
# 安装Apache2  
RUN ( yum install httpd -y ;\  
yum clean all ;\  
rm -rf /var/cache/yum)  
  
# 安装编译组件  
RUN ( yum install git gcc gcc-c++ make -y ;\  
yum clean all ;\  
rm -rf /var/cache/yum )  
  
# 编译安装  
RUN ( cd /tmp ;\  
git clone https://github.com/tenyue/ServerStatus.git ;\  
cd /tmp/ServerStatus/server ;\  
make ;\  
cp -f sergate /usr/sbin/sergate )  
  
# Apache2配置  
RUN ( sed -i "s/AllowOverride None/AllowOverride All/g"
/etc/httpd/conf/httpd.conf ;\  
sed -i "/mod_rewrite.so/s/#LoadModule/LoadModule/" /etc/httpd/conf/httpd.conf
;\  
sed -i "s/\/var\/www\/html/\/ServerStatus\/web\//g" /etc/httpd/conf/httpd.conf
;\  
sed -i "s/\/var\/www/\/ServerStatus\/web\//g" /etc/httpd/conf/httpd.conf )  
  
# ServerStatus配置  
RUN ( mkdir -p /ServerStatus/web ;\  
mkdir -p /ServerStatus/config ;\  
cp -f /tmp/ServerStatus/server/config.json /ServerStatus/config/config.json )  
  
# 网站目录  
RUN ( cp -rf /tmp/ServerStatus/web/* /ServerStatus/web/ ;\  
chmod -R 755 /ServerStatus/web/ ;\  
chown -R apache:apache /ServerStatus/web/ )  
  
# 添加控制脚本  
ADD scripts/sergate_start /usr/sbin/sergate_start  
ADD scripts/sergate_stop /usr/sbin/sergate_stop  
RUN ( chmod +x /usr/sbin/sergate_start ;\  
chmod +x /usr/sbin/sergate_stop )  
  
# 实验性清理  
RUN ( yum history undo 4 -y )  
  
# 清理环境  
RUN ( yum remove make gcc gcc-c++ git -y ;\  
yum clean all ;\  
rm -rf /var/cache/yum ;\  
rm -rf /tmp/ServerStatus )  
  
# 开发端口  
EXPOSE 80 35601  
# 持久化存储  
VOLUME [ "/ServerStatus/config/" ]  
  
# 启动命令行  
ADD entrypoint.sh /usr/sbin/entrypoint.sh  
CMD [ "sh", "/usr/sbin/entrypoint.sh" ]

