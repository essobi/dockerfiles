FROM composer/composer  
MAINTAINER Marc Pantel <pantel.m@gmail.com>  
  
WORKDIR /tmp  
  
RUN curl -LOS
"https://github.com/spress/Spress/releases/download/v2.0.0/spress.phar"  
RUN chmod +x spress.phar  
RUN mv spress.phar /usr/local/bin/spress  
  
VOLUME ["/app"]  
WORKDIR /app  
  
EXPOSE 4000  
CMD ["spress"]  
ENTRYPOINT ["spress"]  

