FROM praekeltfoundation/python-base:latest  
  
COPY . /app/  
RUN pip install -e /app/  
  
CMD ["portia", "run", "--cors", "*", "--web-endpoint", "tcp:8000"]  

