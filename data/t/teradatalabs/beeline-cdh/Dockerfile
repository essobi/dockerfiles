FROM java:8-jre  
  
MAINTAINER hugues@sutoiku.com  
  
COPY . /apps/beeline  
  
ENV HIVE_VERSION 1.1.0  
WORKDIR /apps/beeline  
  
RUN addgroup --gid 40561 stoic && useradd --gid 40561 --uid 40561 stoic && \  
sh lib/download.sh  
  
USER stoic  
ENTRYPOINT /apps/beeline/beeline.sh  

