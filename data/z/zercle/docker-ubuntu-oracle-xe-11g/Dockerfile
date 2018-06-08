FROM zercle/docker-ubuntu  
MAINTAINER bouroo <bouroo@gmail.com>  
  
ENV VERSION='11.2.0-1.0'  
# Update OS  
RUN apt update && apt -y full-upgrade  
  
COPY ./files /  
RUN chmod +x /root/oracle-xe-11g/setup.sh && bash /root/oracle-xe-11g/setup.sh  
RUN chmod +x /root/entrypoint.sh  
  
EXPOSE 22 1521 8080  
ENTRYPOINT ["/root/entrypoint.sh"]  

