FROM python:3.6  
WORKDIR /app/goldsgym  
  
COPY requirements.txt /app/goldsgym/requirements.txt  
COPY constraints.txt /app/goldsgym/constraints.txt  
  
RUN pip install -r requirements.txt -c constraints.txt  
  
COPY . /app/goldsgym  
  
CMD ["python", "."]  

