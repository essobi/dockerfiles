FROM picorb/rabbitmq-base:ubuntu  
MAINTAINER Biju Kunjummen biju.kunjummen@gmail.com  
  
RUN mkdir /opt/rabbit  
  
ADD startrabbit.sh /opt/rabbit/  
  
RUN chmod a+x /opt/rabbit/startrabbit.sh  
  
EXPOSE 5672  
EXPOSE 15672  
EXPOSE 25672  
EXPOSE 4369  
EXPOSE 9100 9101 9102 9103 9104 9105  
CMD ["/opt/rabbit/startrabbit.sh"]  

