FROM python:3.4-slim  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY requirements.txt /usr/src/app/requirements.txt  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . /usr/src/app/  
  
EXPOSE 8080  
CMD ["/usr/local/bin/gunicorn", "-k", "tornado", "app:app", "--bind",
"0.0.0.0:8080"]

