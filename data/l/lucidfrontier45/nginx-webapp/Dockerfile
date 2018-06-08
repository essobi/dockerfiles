FROM nginx  
LABEL maintainer="Shiqiao Du <lucidfrontier.45@gmail.com>"  
  
RUN ["mkdir", "/webapp"]  
  
COPY docker-entrypoint.sh /  
COPY nginx /etc/nginx/conf.d  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
ENV API_URL "http://127.0.0.1:8080/api/"  
EXPOSE 443  
STOPSIGNAL SIGQUIT  
  
CMD ["nginx", "-g", "daemon off;"]

