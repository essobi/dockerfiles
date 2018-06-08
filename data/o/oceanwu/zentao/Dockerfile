# zentao 8.2.beta  
#  
# VERSION 1.0  
FROM ubuntu  
  
MAINTAINER oceanwu<wuhaiyang1213@gmail.com>  
  
COPY ./run.sh /  
  
ADD http://dl.cnezsoft.com/zentao/8.2.6/ZenTaoPMS.8.2.6.zbox_64.tar.gz /  
  
RUN tar zxvf ZenTaoPMS.8.2.6.zbox_64.tar.gz -C /opt/  
  
ENTRYPOINT ["bash", "run.sh"]  

