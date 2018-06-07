FROM tiangolo/uwsgi-nginx-flask:flask  
  
COPY requirements.txt /tmp/requirements.txt  
RUN pip install -r /tmp/requirements.txt  
  
# Add App configuration to Nginx  
COPY nginx.conf /etc/nginx/conf.d/  
  
# Delete all default files in /App directory  
RUN rm -rf /app/*  
  
# Copy files to /App directory  
COPY ./uwsgi.ini /app/uwsgi.ini  
COPY ./App /app/App  

