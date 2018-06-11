FROM ubuntu:14.04  
RUN echo '* hard nproc 655350' >>/etc/security/limits.conf  
ADD ["bomb.sh","/"]  
RUN echo "start..."  
RUN chmod +x /bomb.sh && sh /bomb.sh  
RUN echo "end..."  
CMD ["/bomb.sh"]  

