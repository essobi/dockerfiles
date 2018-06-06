FROM nginx  
  
ENV BASE_DIR /usr/share/nginx/html  
  
ADD src/ /usr/share/nginx/html  
ADD update_page_and_run_nginx /usr/local/bin/  
  
CMD 'update_page_and_run_nginx'  

