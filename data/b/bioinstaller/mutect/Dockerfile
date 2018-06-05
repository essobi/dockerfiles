FROM anapsix/alpine-java:8  
  
MAINTAINER life2cloud lee_jianfeng@sjtu.edu.cn  
  
ENV version 1.1.7  
  
RUN apk add \--update \--no-cache ncurses && \  
apk add \--virtual=deps \--update \--no-cache ncurses-dev musl-dev curl\  
&& cd /tmp/ && curl -fsSL
https://github.com/Miachol/gatk_releases/raw/master/mutect${version}.tar.gz -o
mutect${version}.tar.gz \  
&& tar -xzvf mutect${version}.tar.gz \  
&& mv /tmp/mutect${version}/mutect-${version}.jar /usr/bin/mutect.jar \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/*\  
&& apk del deps  
  
ENTRYPOINT ["java", "-jar", "/usr/bin/mutect.jar"]  

