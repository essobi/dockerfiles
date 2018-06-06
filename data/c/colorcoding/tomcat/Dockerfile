# 基于官方tomcat镜像  
FROM tomcat:8.5-alpine  
  
# 维护者  
LABEL maintainer="Niuren.Zhu <niuren.zhu@icloud.com>"  
  
# 安装工具  
RUN set -x \  
# 更新源  
&& apk update \  
# 安装解压、网络请求、时区设置  
&& apk add \--no-cache unzip curl tzdata \  
# 安装字体  
&& apk add \--no-cache fontconfig ttf-dejavu \  
# 删除源  
&& rm -rf /var/cache/apk/*  
  
# 创建数据文件夹  
RUN set -x \  
&& mkdir -p ${CATALINA_HOME}/ibas \  
&& mkdir -p ${CATALINA_HOME}/ibas/conf \  
&& mkdir -p ${CATALINA_HOME}/ibas/data \  
&& mkdir -p ${CATALINA_HOME}/ibas/logs \  
&& mkdir -p ${CATALINA_HOME}/ibas_tools \  
&& rm -rf ${CATALINA_HOME}/webapps \  
&& mkdir -p ${CATALINA_HOME}/webapps  
  
# 下载并部署工具  
RUN set -x \  
&& curl -fsSL -o /tmp/btulz.transforms.tar
http://maven.colorcoding.org/repository/maven-
releases/org/colorcoding/tools/btulz.transforms/latest/btulz.transforms-
latest.tar \  
&& tar -xvf /tmp/btulz.transforms.tar -C ${CATALINA_HOME}/ibas_tools \  
&& rm -f /tmp/btulz.transforms.tar  
  
# 拷贝配置文件  
COPY conf/* ${CATALINA_HOME}/conf/  
COPY ibas/ ${CATALINA_HOME}/ibas/  
COPY deploy_apps.sh ${CATALINA_HOME}/deploy_apps.sh  
COPY initialize_apps.sh ${CATALINA_HOME}/initialize_apps.sh  
  
RUN chmod 775 ${CATALINA_HOME}/*.sh  
  
VOLUME ${CATALINA_HOME}/ibas/  

