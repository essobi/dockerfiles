FROM nginx:stable  
  
WORKDIR /opt  
  
COPY ./entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["nginx", "-g", "daemon off;"]

