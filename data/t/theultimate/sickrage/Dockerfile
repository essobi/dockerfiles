FROM theultimate/mediabase  
MAINTAINER Maikel Dollé <maikel@itmagix.nl>  
  
RUN git clone \--depth 1 https://github.com/SickRage/SickRage.git /sickrage  
  
ADD ./sickrage_config.ini /sickrage/  
ADD ./start.sh /start.sh  
  
RUN chmod u+x /start.sh  
  
EXPOSE 9400  
CMD ["./start.sh"]  

