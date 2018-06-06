FROM mhoush/psycopg2  
  
ADD . /app  
  
RUN pip install --upgrade /app \  
pytest \  
pytest-cov  
  
WORKDIR /app  
  
CMD ["/usr/bin/make", "run-example"]  

