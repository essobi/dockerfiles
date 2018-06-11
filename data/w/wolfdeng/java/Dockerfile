# Alpine Linux with and Oracle Java 8  
FROM anapsix/alpine-java:8u144b01_jdk  
  
MAINTAINER Tony Deng ( wolf.deng@gmail.com )  
  
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g'
/etc/apk/repositories  
  
VOLUME ["/opt/jdk"]  

