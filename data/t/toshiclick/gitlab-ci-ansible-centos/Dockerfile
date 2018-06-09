FROM centos:7  
# 作成者情報  
MAINTAINER toshi <toshi@toshi.click>  
  
# EPELを導入しておく + yum update + editor install  
RUN echo "include_only=.jp" >> /etc/yum/pluginconf.d/fastestmirror.conf && \  
yum -q clean all && \  
yum -y -q install epel-release && \  
yum -y -q update && \  
rm -f /etc/rpm/macros.image-language-conf && \  
sed -i '/^override_install_langs=/d' /etc/yum.conf && \  
yum reinstall -y -q glibc-common && \  
yum -y -q groupinstall "Development Tools" && \  
yum install -y -q vim kbd ibus-kkc vlgothic-* && \  
yum -q clean all  
  
# set ENV  
ENV container docker \  
LANG=ja_JP.UTF-8 \  
LANGUAGE=ja_JP:ja \  
LC_ALL=ja_JP.UTF-8  
  
RUN localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 && \  
echo 'LANG="ja_JP.UTF-8"' > /etc/locale.conf && \  
echo 'ZONE="Asia/Tokyo"' > /etc/sysconfig/clock && \  
unlink /etc/localtime && \  
ln -s /usr/share/zoneinfo/Japan /etc/localtime  
  
RUN yum install -y ansible systemd libselinux-python selinux-policy && yum
clean all  
  
# CIテスト用にsystemdを有効にする  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \  
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
VOLUME [ "/sys/fs/cgroup" ]  
  
# CIサーバーからsshの警告が出ないように設定を追加する  
ADD ansible.cfg /etc/ansible/ansible.cfg  
# CIサーバーが国内なのでJP限定にする  
ADD fastestmirror.conf /etc/yum/pluginconf.d/fastestmirror.conf  
  
CMD ["/usr/sbin/init"]  

