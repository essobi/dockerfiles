FROM python:3.6  
ARG project_dir=/web/  
  
RUN apt update -y && apt upgrade -y && apt install -y mariadb-client
postgresql-client  
  
WORKDIR $project_dir  
VOLUME ["/web"]  
EXPOSE 5000  
COPY entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/entrypoint.sh  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["python app.py"]  

