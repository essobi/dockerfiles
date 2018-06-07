FROM tiangolo/uwsgi-nginx:python3.5  
COPY ./requirements.txt /tmp/  
RUN pip install -r /tmp/requirements.txt && \  
rm /tmp/requirements.txt  
  
# Add app configuration to Nginx  
COPY nginx.conf /etc/nginx/conf.d/  
  
# Copy sample app  
COPY ./app /app  

