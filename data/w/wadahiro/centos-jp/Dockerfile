FROM centos:6.8  
LABEL maintainer "Hiroyuki Wada <wadahiro@gmail.com>"  
  
RUN yum groupinstall -y "Japanese Support" && yum reinstall -y glibc-common &&
yum clean all  
  
RUN echo 'ZONE="Asia/Tokyo"' > /etc/sysconfig/clock  
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
  
RUN echo 'LANG="ja_JP.UTF-8"' > /etc/sysconfig/i18n  
RUN echo 'LC_CTYPE="ja_JP.utf8"' >> /etc/sysconfig/i18n  
  
RUN localedef -f UTF-8 -i ja_JP /usr/lib/locale/ja_JP.UTF-8  
  
ENV LC_ALL ja_JP.UTF-8  
ENV LANG ja_JP.UTF-8  
ENV TZ Asia/Tokyo  
  
  
CMD "/bin/bash"  

