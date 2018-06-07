######################  
# PHPLOC in a docker container  
######################  
FROM php  
RUN mkdir /app  
COPY phploc.phar /usr/local/bin/phploc  
RUN chmod 777 /usr/local/bin/phploc /app  
VOLUME [ "/app" ]  
WORKDIR /app  
ENTRYPOINT [ "phploc" ]  

