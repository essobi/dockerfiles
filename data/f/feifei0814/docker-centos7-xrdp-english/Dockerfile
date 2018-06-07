FROM centos:7  
ENV container docker  
  
RUN yum update -y  
RUN yum groupinstall -y "Minimal Install"  
RUN yum install -y epel-release  
RUN yum groupinstall -y "Xfce"  
RUN yum groupinstall -y "Development Tools"  
RUN yum install -y R firefox bwa samtools xrdp tigervnc-server vlgothic-fonts
ipa-mincho-fonts ipa-gothic-fonts ipa-pmincho-fonts ipa-pgothic-fonts net-
tools zsh libevent ibus-kkc file bind-utils vcftools bedtools supervisor
vlgothic-p-fonts libxml2 mock gcc rpm-build rpm-devel rpmlint make python bash
coreutils diffutils patch rpmdevtools traceroute vim wget gedit  
  
RUN yum remove -y NetworkManager ctags  
ADD rpms/emacs25-25.2-1.el7.centos.x86_64.rpm /  
RUN yum install -y ./emacs25-25.2-1.el7.centos.x86_64.rpm  
  
RUN yum -y install kde-l10n-Chinese && yum -y reinstall glibc-common #安装中文支持  
RUN localedef -v -c -i zh_CN -f UTF-8 zh_CN.UTF-8; echo ""; #配置显示中文  
  
#修改root用户密码  
RUN echo "root:qwe123!@#" | chpasswd  
  
#install 安装支持中文的字体  
ADD chinese-font.sh /  
RUN /bin/bash -xe /chinese-font.sh  
  
#设置远程桌面  
ADD setupcontainer.sh /  
RUN /bin/bash -xe /setupcontainer.sh  
  
#删除安装包  
RUN rm -rf /chinese-font.sh  
RUN rm -rf /setupcontainer.sh  
RUN rm -rf /emacs25-25.2-1.el7.centos.x86_64.rpm  
RUN rm -rf /wqy-microhei-0.2.0-beta.tar.gz  
RUN rm -rf /wqy-microhei  
  
#设置用户与xfce桌面  
ADD entrypoint.sh /  
EXPOSE 3389  
VOLUME /home  
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]  

