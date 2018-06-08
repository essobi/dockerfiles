FROM anapsix/alpine-java:8  
MAINTAINER life2cloud lee_jianfeng@sjtu.edu.cn  
  
ENV version 2.13.2  
ADD
https://github.com/broadinstitute/picard/releases/download/${version}/picard.jar
/opt  
  
ENTRYPOINT ["java", "-jar", "/opt/picard.jar"]  

