FROM tutum/apache-php  
ADD ./wln /wln  
RUN mv /wln/run.sh / && chmod -R 777 /run.sh && rm -fr /app/*  
EXPOSE 80  
VOLUME ["/app/data/"]  
VOLUME ["/app/data/User/wlniao/home/"]

