FROM nginx  
RUN sed -i 's/^http {/&\n server_names_hash_bucket_size 128;/g'
/etc/nginx/nginx.conf  
RUN sed -i 's/^http {/&\n variables_hash_bucket_size 128;/g'
/etc/nginx/nginx.conf  

