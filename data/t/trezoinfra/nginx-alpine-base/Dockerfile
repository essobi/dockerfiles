FROM mortimor/nginx-pagespeed  
  
#Add www-data user and group with IDs 82  
RUN usermod www-data -u 82; groupmod -g 82 www-data;  
  
#Add deploy user with UID 2500  
RUN useradd deploy -u 2500 -g www-data -s /bin/bash  
  
ADD ./entrypoint.sh /entrypoint.sh  
RUN chmod u+x /entrypoint.sh  
ENTRYPOINT ["sh", "/entrypoint.sh"]  

