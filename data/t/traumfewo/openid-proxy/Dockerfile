FROM python:3.6-slim  
  
EXPOSE 5000  
COPY requirements.txt openid-proxy.py ./  
  
RUN pip install -r requirements.txt  
  
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3", "openid-
proxy:app"]  

