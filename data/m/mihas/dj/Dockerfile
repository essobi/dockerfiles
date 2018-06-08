FROM mihas/civic-deps  
  
RUN apt-get install -y python-psycopg2  
  
ADD ./requirements.txt .  
RUN pip install -r requirements.txt  
  
EXPOSE 8000  

