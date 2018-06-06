FROM python:3.6  
WORKDIR /app  
  
COPY requirements.txt /app/requirements.txt  
COPY constraints.txt /app/constraints.txt  
  
RUN pip install -r requirements.txt -c constraints.txt  
  
COPY exchanges.yml /app/exchanges.yml  
COPY exchange-data-loader.py /app/exchange-data-loader.py  
  
CMD ["python", "exchange-data-loader.py"]  

