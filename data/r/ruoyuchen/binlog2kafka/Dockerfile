FROM maven:3-ibmjava-8-alpine as jar_builder  
RUN apk add --no-cache bash git && git clone
https://github.com/ruoyuchen/binlog2kafka.git && cd binlog2kafka && mvn
package  
  
FROM java:openjdk-8-jre-alpine  
MAINTAINER Will Chen <willcup@163.com>  
RUN apk add --no-cache bash curl tree tzdata && cp
/usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
COPY /SysConfig.properties_template .  
COPY \--from=jar_builder /binlog2kafka/target/will_sync-1.0.2.jar
/will_sync-1.0.2.jar  
COPY /start.sh .  
ENTRYPOINT ["sh", "start.sh"]  

