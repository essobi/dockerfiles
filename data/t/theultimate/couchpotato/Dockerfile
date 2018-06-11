FROM theultimate/mediabase  
MAINTAINER Maikel Dollé <maikel@itmagix.nl>  
  
RUN cd ~ && \  
git clone \--depth 1 https://github.com/RuudBurger/CouchPotatoServer.git
/CouchPotatoServer  
  
ADD ./start.sh /start.sh  
ADD ./settings.conf /CouchPotatoServer  
  
RUN chmod u+x /start.sh  
  
EXPOSE 9500  
CMD ["./start.sh"]  

