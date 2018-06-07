FROM examus/base  
  
ENV PYTHONUNBUFFERED 1  
WORKDIR /app  
COPY . /app  
COPY ./docker-entrypoint.sh /bin/docker-entrypoint.sh  
RUN chmod +x /app/docker-prepare.sh /bin/docker-entrypoint.sh && bash
/app/docker-prepare.sh  
  
EXPOSE 8555  
ENTRYPOINT ["/bin/docker-entrypoint.sh"]  

