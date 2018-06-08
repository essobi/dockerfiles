FROM anapsix/alpine-java:8  
  
MAINTAINER life2cloud lee_jianfeng@sjtu.edu.cn  
  
ENV version 3.8-0  
  
RUN apk add \--update \--no-cache ncurses && \  
apk add \--virtual=deps \--update \--no-cache ncurses-dev musl-dev curl\  
&& cd /tmp/ && curl -fsSL
https://github.com/Miachol/gatk_releases/raw/master/gatk${version}.tar.gz -o
gatk${version}.tar.gz \  
&& tar -xzvf gatk${version}.tar.gz \  
&& mv /tmp/gatk${version}/GenomeAnalysisTK.jar /usr/bin/ \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/* \  
&& apk del deps  
  
ENTRYPOINT ["java", "-jar", "/usr/bin/GenomeAnalysisTK.jar"]  

