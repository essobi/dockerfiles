FROM omarsmak/python-mongodb-base-image:2.7-3.0  
ENV DATABASE_PORT 27017  
ENV DATABASE_HOST '127.0.0.1'  
ENV APP_PORT 27001  
ENV DATABASE_NAME 'ids_connector'  
ENV DATASET_FILE_NAME 'dataset'  
COPY . /app  
WORKDIR /app  
  
RUN pip install -r requirements.txt \  
&& python setup.py install \  
&& sh -c 'chmod +x run.sh'  
  
EXPOSE ${APP_PORT}  
  
ENTRYPOINT ["/app/run.sh"]  

