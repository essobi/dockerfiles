FROM phpmyadmin/phpmyadmin  
MAINTAINER "Hiroki Takeyama"  
# mysql info  
ENV PMA_HOST 192.168.1.1  
ENV PMA_PORT 3306  
ENV PMA_USER root  
ENV PMA_PASSWORD root  
  
EXPOSE 80  
ENTRYPOINT ["/run.sh"]  
  
CMD ["phpmyadmin"]  

