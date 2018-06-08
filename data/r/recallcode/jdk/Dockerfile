FROM anapsix/alpine-java:8u172b11_jdk_unlimited  
  
ENV TZ=Asia/Shanghai  
  
RUN mkdir -p /usr/share/zoneinfo/Asia  
  
COPY Shanghai /usr/share/zoneinfo/Asia  
  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  

