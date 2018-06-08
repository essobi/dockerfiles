FROM frosner/luigi-base  
  
RUN mkdir /etc/service/luigid  
ADD luigid.sh /etc/service/luigid/run  
RUN chmod a+x /etc/service/luigid/run  
  
CMD ["/sbin/my_init"]  

