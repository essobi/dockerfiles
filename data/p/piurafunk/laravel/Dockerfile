FROM php:5.6-alpine  
ARG VERBOSE  
ARG UID=1000  
WORKDIR /home/laravel/app  
  
COPY buildscript /  
RUN chmod +x /buildscript  
RUN /buildscript  
  
COPY startupscript /  
RUN chmod +x /startupscript  
  
USER laravel  
ENV PATH $PATH:/usr/local/share/nodejs/bin  
  
EXPOSE 80 443  
ENTRYPOINT ["/startupscript"]  

