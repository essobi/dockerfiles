FROM index.tenxcloud.com/revolc/openjdk8-jre:latest  
  
MAINTAINER 张仪 <wittcnezh@foxmail.com>  
  
WORKDIR /opt  
  
RUN curl -skSL http://edas-public.oss-cn-
hangzhou.aliyuncs.com/install_package/edas-config-center.zip -o /tmp/tmp.zip
&& \  
unzip -x /tmp/tmp.zip && \  
rm -rf /tmp/*  
  
WORKDIR /opt/edas-config-center  
  
ADD run.sh /opt/edas-config-center/  
  
EXPOSE 8080 9600  
CMD [ "/bin/sh", "run.sh" ]  

