FROM python:3.5-jessie  
  
RUN pip install gamification-engine \  
&& pip install gamification-engine[auth,pushes,testing] \  
&& gengine_quickstart app  
  
COPY docker-entrypoint.sh /usr/local/bin  
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-
it.sh /usr/local/bin/wait-for-it.sh  
RUN chmod +x /usr/local/bin/*.sh  
  
WORKDIR /app  
  
EXPOSE 6543  
CMD ["/usr/local/bin/docker-entrypoint.sh"]  

