FROM python:3.5  
WORKDIR /app/anti-captcha  
  
COPY . .  
RUN pip install --no-cache-dir -r requirements.txt  
  
CMD ["uwsgi", "uwsgi.ini"]

