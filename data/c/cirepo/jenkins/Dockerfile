  
# from alpine:3.7 or debian:stretch-slim (version without -alpine)  
FROM jenkins/jenkins:2.124-alpine  
  
USER root  
# see: http://wiki.alpinelinux.org/wiki/Setting_the_timezone  
RUN echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.7/main" >
/etc/apk/repositories && \  
echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.7/community" >>
/etc/apk/repositories && \  
echo "https://mirror.tuna.tsinghua.edu.cn/alpine/edge/testing/" >>
/etc/apk/repositories && \  
apk --update add tzdata && \  
apk add libstdc++ bash aria2 && \  
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
echo "Asia/Shanghai" > /etc/timezone && \  
apk del tzdata && \  
rm -rf /tmp/* /var/cache/apk/* && \  
echo "UTC+8:00" > /etc/TZ  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
USER ${user}  
#RUN cat /usr/local/bin/plugins.sh  
COPY docker/plugins.sh /usr/local/bin/plugins.sh  
COPY docker/plugins.txt /usr/share/jenkins/plugins.txt  
#ENV JENKINS_UC_DOWNLOAD http://updates.jenkins-ci.org/download  
#ENV JENKINS_UC_DOWNLOAD http://ftp.yz.yamagata-u.ac.jp/pub/misc/jenkins  
ENV JENKINS_UC_DOWNLOAD https://mirrors.tuna.tsinghua.edu.cn/jenkins  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  
  
#COPY docker/plugins/*.hpi /usr/share/jenkins/ref/plugins  
COPY docker/executors.groovy
/usr/share/jenkins/ref/init.groovy.d/executors.groovy  
COPY docker/custom.groovy /usr/share/jenkins/ref/init.groovy.d/custom.groovy  

