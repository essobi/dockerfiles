FROM java:8  
MAINTAINER Leo Hu <mail@huzhonghua.cn>  
  
RUN cp -n /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
RUN echo "deb http://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list  
RUN apt-key update  
RUN apt-get update  
RUN apt-get -y --force-yes install sbt  
  
EXPOSE 9000 8888  
RUN mkdir /blog  
WORKDIR /blog  
  
RUN apt-get install -y git  
RUN apt-get install -y vim  
  
RUN git clone https://github.com/1993hzh/blogV2.git /blog  
RUN cd /blog && sbt compile  

