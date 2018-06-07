FROM theultimate/mediabase  
MAINTAINER Maikel Dollé <maikel@itmagix.nl>  
  
RUN git clone \--depth 1 https://github.com/DobyTang/LazyLibrarian.git
/lazylibrarian  
  
ADD ./config.ini /lazylibrarian  
ADD ./start.sh /start.sh  
  
RUN chmod u+x /start.sh  
  
EXPOSE 9700  
CMD ["./start.sh"]  

