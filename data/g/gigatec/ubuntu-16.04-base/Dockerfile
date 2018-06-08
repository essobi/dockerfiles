FROM ubuntu:16.04  
ADD base/init.sh /init.sh  
ADD base/run.sh /run.sh  
  
RUN groupadd -g 1000 vagrant  
RUN useradd -u 1000 -g vagrant vagrant  
  
RUN /init.sh  
  
ADD files/usr/local/bin /usr/local/bin  
ADD files/root /root  
  
CMD /run.sh  

