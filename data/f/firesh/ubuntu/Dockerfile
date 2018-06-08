FROM ubuntu:xenial  
  
# 设置时区  
ENV TZ=Asia/Shanghai  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# 中文支持  
RUN locale-gen zh_CN.UTF-8 &&\  
DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales  
RUN locale-gen zh_CN.UTF-8  
ENV LANG zh_CN.UTF-8  
ENV LANGUAGE zh_CN:zh  
ENV LC_ALL zh_CN.UTF-8  
# 更改软件源  
RUN sed -i 's/archive.ubuntu.com/mirrors.aliyun.com/' /etc/apt/sources.list  

