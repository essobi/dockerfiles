FROM debian:wheezy  
  
ENV HOME /root  
ADD ./build /build  
  
RUN /build/prepare.sh  
  
ADD set_root_pw.sh /set_root_pw.sh  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
ENV AUTHORIZED_KEYS **None**  
  
EXPOSE 22  
CMD ["/run.sh"]  

