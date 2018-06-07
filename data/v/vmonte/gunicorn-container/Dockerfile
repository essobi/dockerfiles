FROM vmonte/python3.5-psycopg2  
  
ADD requirement.txt ${BASE_PROJECT_FOLDER}  
RUN pip install -r ${BASE_PROJECT_FOLDER}/requirement.txt  
  
COPY ./gunicorn.sh /  
RUN chmod 777 /gunicorn.sh  
  
ENTRYPOINT ["/gunicorn.sh"]  

