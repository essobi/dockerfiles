FROM nginx:1.13.5-alpine  
  
ADD entrypoint.sh /usr/local/bin  
  
ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]  
CMD [ "nginx", "-g", "daemon off;" ]  

