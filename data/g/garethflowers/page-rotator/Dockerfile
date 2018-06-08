FROM php:7.2.0-alpine  
  
CMD [ "php", "-t", "public", "-S", "0.0.0.0:80",
"/usr/src/app/common/router.php" ]  
EXPOSE 80  
HEALTHCHECK CMD wget --spider http://localhost || exit 1  
VOLUME [ "/usr/src/app/config" ]  
WORKDIR "/usr/src/app"  
  
COPY [ "./src", "/usr/src/app/" ]  

