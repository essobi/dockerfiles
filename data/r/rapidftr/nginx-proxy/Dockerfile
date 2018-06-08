FROM ubuntu:14.04  
VOLUME /data  
EXPOSE 80  
EXPOSE 443  
EXPOSE 6984  
EXPOSE 5984  
COPY app/provision.sh /app/  
RUN /app/provision.sh  
  
COPY app/Procfile /app/  
COPY app/nginx.tmpl /app/  
COPY app/reload.sh /app/  
  
WORKDIR /app  
CMD ["forego", "start", "-r"]  

