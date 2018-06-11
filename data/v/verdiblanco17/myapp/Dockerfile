FROM python:3.5-alpine  
  
MAINTAINER Y.Sugita  
  
WORKDIR /app  
  
EXPOSE 8080  
RUN pip install gunicorn  
  
ADD app.py /app/  
  
CMD ["gunicorn", "app:application", "-b", ":8080"]

