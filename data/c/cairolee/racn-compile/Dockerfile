# 基础镜像  
FROM centos:6.9  
# 维护人员  
MAINTAINER CairoLee "cairoliyu@gmail.com"  
# 安装必要的 scl 源  
RUN yum install centos-release-scl -y  
  
# 修改系统时区为 UTC+8:00  
RUN yum install -y ntpdate \  
&& \cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& yum -y install kde-l10n-Chinese \  
&& yum -y reinstall glibc-common \  
&& sed -i 's/LANG="en_US.UTF-8"/LANG="zh_CN.UTF-8"/g' /etc/sysconfig/i18n \  
&& echo 'SUPPORTED="zh_CN.UTF-8:zh_CN:zh:en_US.UTF-8:en_US:en"' >>
/etc/sysconfig/i18n  
  
# 安装 gcc 6.x 开发者工具包 和 必要的其他工具  
RUN yum install devtoolset-6 -y \  
&& yum install git gdb screen unzip zip vim -y \  
&& yum install mysql-devel pcre-devel zlib-devel -y  
  
# 设置环境变量  
ENV PATH="/opt/rh/devtoolset-6/root/usr/bin:${PATH}"  
# 清理工作  
RUN rm -rf /root/*  
  
# 设置入口  
CMD ["bin/bash"]  

