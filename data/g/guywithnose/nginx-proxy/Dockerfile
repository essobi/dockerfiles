FROM jwilder/nginx-proxy  
  
ADD nginx.tmpl /app/nginx.tmpl  
  
ADD nginxEnvVars /app/nginxEnvVars  
  
CMD /app/nginxEnvVars && forego start -r > /dev/null  

