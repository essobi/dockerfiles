FROM zingsono/openjdk:1.8-jre  
MAINTAINER Zengs.<zingsono@gmail.com>  
  
WORKDIR /es  
  
# 1. 下载elasticsearch 压缩包并解压  
RUN curl -o es.tar.gz
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.4.tar.gz
&& tar -xf es.tar.gz --strip-components=1 && rm -f es.tar.gz  
  
# 2. 设置环境变量  
ENV PATH=$PATH:/es/bin/  
  
# 3. 创建es用户，设置/es目录的所有者为es用户  
RUN adduser --user-group es && chown -R es:es /es  
  
# 4. 切换用户  
USER es  
  
# 数据卷 docker volume create elasticsearch  
# es目录中内容为默认解压文件，修改配置，可直接在数据卷中修改  
# docker run -v elasticsearch:/es zingsono/elasticsearch:6.2.4  
VOLUME /es/  
  
EXPOSE 9200 9300  
# Version: 6.2.4, Build: ccec39f/2018-04-12T20:37:28.497551Z, JVM: 1.8.0_171  
RUN elasticsearch --version  
  
CMD ["elasticsearch"]  

