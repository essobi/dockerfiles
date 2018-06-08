FROM phusion/baseimage:0.9.18  
MAINTAINER lilingv@gmail.com  
  
# Setup timezone  
RUN echo Asia/Shanghai > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata  
  
# Setup locale  
RUN locale-gen en_US.UTF-8 && locale-gen zh_CN.UTF-8 && locale-gen zh_CN &&
locale-gen zh_CN.GBK && locale-gen zh_CN.GB18030  
  
# Install packages  
RUN apt-get update; apt-get -y upgrade; apt-get install -y lftp curl wget
dstat dnsutils rlwrap  
  
# Setup locale  
ENV LC_CTYPE="zh_CN.UTF-8"  
ENV LC_NUMERIC="zh_CN.UTF-8"  
ENV LC_TIME="zh_CN.UTF-8"  
ENV LC_COLLATE="zh_CN.UTF-8"  
ENV LC_MONETARY="zh_CN.UTF-8"  
ENV LC_MESSAGES="en_US.UTF-8"  
ENV LC_PAPER="zh_CN.UTF-8"  
ENV LC_NAME="zh_CN.UTF-8"  
ENV LC_ADDRESS="zh_CN.UTF-8"  
ENV LC_TELEPHONE="zh_CN.UTF-8"  
ENV LC_MEASUREMENT="zh_CN.UTF-8"  
ENV LC_IDENTIFICATION="zh_CN.UTF-8"  
# Setup oracle  
RUN apt-get install -y libaio-dev  
ADD oracle/*.deb /tmp/  
RUN dpkg -i /tmp/*.deb  
RUN rm -f /tmp/*.deb  
ADD oracle/*.jar /usr/lib/oracle/12.1/client64/lib/  
ENV ORACLE_HOME /usr/lib/oracle/12.1/client64  
ENV NLS_LANG "SIMPLIFIED CHINESE_CHINA.AL32UTF8"  
ADD oracle/ld_oracle.conf /etc/ld.so.conf.d/oracle.conf  
RUN ldconfig  
  
# Add profile  
ADD rlwrap.sh /etc/profile.d  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

