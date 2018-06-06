# 基于镜像alpine  
FROM colorcoding/compiling:ibas-alpine  
  
# 维护者  
LABEL maintainer="Niuren.Zhu <niuren.zhu@icloud.com>"  
  
# 更新环境  
RUN set -x \  
# 更新源  
&& apk update \  
# 安装CURL  
&& apk add \--no-cache curl \  
# 安装UNZIP  
&& apk add \--no-cache unzip \  
# 删除源  
&& rm -rf /var/cache/apk/*  
  
# 工具版本  
ARG GIT_TF_VERSION=2.0.3.20131219  
# 安装工具  
RUN set -x \  
# 下载GIT-TF  
&& curl -sL
https://download.microsoft.com/download/A/E/2/AE23B059-5727-445B-91CC-15B7A078A7F4/git-
tf-${GIT_TF_VERSION}.zip -O \  
# 解压安装  
&& unzip -o git-tf-${GIT_TF_VERSION}.zip -d /usr/share/ \  
&& ln -s /usr/share/git-tf-${GIT_TF_VERSION}/git-tf /usr/bin/git-tf \  
# 删除文件  
&& rm -rf ./git-tf-${GIT_TF_VERSION}.zip  
  
# 设置环境变量  
ENV GITTF_HOME /usr/share/git-tf-${GIT_TF_VERSION}/  

