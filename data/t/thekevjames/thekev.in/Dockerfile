FROM python:3.5.2-alpine  
  
EXPOSE 5000  
COPY requirements.txt /src/requirements.txt  
RUN pip install --upgrade pip && \  
pip install --no-cache-dir -r /src/requirements.txt  
  
COPY . /src  
  
CMD ["python", "/src/server.py"]  

