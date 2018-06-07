FROM theultimate/mediabase  
MAINTAINER Maikel Dollé <maikel@itmagix.nl>  
  
RUN git clone \--depth 1 https://github.com/rembo10/headphones.git /headphones  
  
ADD ./config.ini /headphones  
ADD ./start.sh /start.sh  
  
RUN chmod u+x /start.sh  
  
EXPOSE 9600  
CMD ["./start.sh"]  

