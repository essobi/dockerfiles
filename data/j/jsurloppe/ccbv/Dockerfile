FROM python:2  
WORKDIR /usr/src/app  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY django-cbv-inspector .  
COPY settings.py ./inspector/  
  
RUN python manage.py migrate cbv  
RUN python manage.py load_all_django_versions  
RUN python manage.py collectstatic  
  
EXPOSE 8000  
CMD ["gunicorn", "-b", "0.0.0.0", "inspector.wsgi"]  

