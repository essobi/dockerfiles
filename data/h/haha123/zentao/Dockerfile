FROM ubuntu:trusty  
  
ADD http://dl.cnezsoft.com/zentao/9.8.3/ZenTaoPMS.9.8.3.zbox_64.tar.gz /tmp  
  
COPY ./boot.sh /usr/local/boot.sh  
RUN chmod +x /usr/local/boot.sh  
  
ENTRYPOINT ["/usr/local/boot.sh"]  

