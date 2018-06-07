FROM kong:0.9.5  
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-
it.sh /usr/local/bin/wait-for-it  
RUN chmod a+x /usr/local/bin/wait-for-it  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  

