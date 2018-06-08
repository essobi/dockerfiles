FROM index.alauda.cn/library/java:openjdk-8-alpine  
MAINTAINER "Longwei Li <longwei.li@moji.com>"  
RUN apk add -U tzdata  
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
WORKDIR /apache-tomcat-7.0.33-SF  
ADD ./apache-tomcat-7.0.33-SF/ /apache-tomcat-7.0.33-SF  
ADD ./run.sh /apache-tomcat-7.0.33-SF/run.sh  
RUN chmod 777 /apache-tomcat-7.0.33-SF/run.sh  
ADD ./hosts_addr /apache-tomcat-7.0.33-SF/hosts_addr  
EXPOSE 7011  
CMD ["/bin/sh","/apache-tomcat-7.0.33-SF/run.sh"]  

