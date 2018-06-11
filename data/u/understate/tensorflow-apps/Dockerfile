FROM python:3.4  
WORKDIR /usr/src/app  
COPY tensorflow_apps ./  
  
RUN pip install -r requirements.txt  
  
EXPOSE 8000  
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

