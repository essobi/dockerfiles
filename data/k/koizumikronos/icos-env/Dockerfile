from centos:6.7  
# timezone  
RUN \cp /etc/sysconfig/clock /etc/sysconfig/clock.org  
RUN echo -e 'ZONE="Asia/Tokyo"\nUTC=false' > /etc/sysconfig/clock  
RUN \cp /etc/localtime /etc/localtime.org  
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
# 言語設定  
RUN \cp /etc/sysconfig/i18n /etc/sysconfig/i18n.origin  
RUN echo 'LANG="ja_JP.UTF-8"' > /etc/sysconfig/i18n  
# 確認  
RUN date  
RUN strings /etc/localtime  
RUN locale  
  
RUN yum install -y tar wget mysql-client fontconfig-devel git unzip  
  
# install java  
ADD install_java /  
RUN ./install_java  
  
# install node  
ADD install_node /  
RUN ./install_node  

