from andaag/large_notebook3  
  
# docker build -t andaag/api-example . && docker run -p 80:80 -ti andaag/api-
example  
RUN apt-get update  
RUN apt-get install -y nginx uwsgi uwsgi-plugin-python3  
RUN update-alternatives --set uwsgi /usr/bin/uwsgi_python34  
  
RUN mkdir -p /etc/uwsgi/apps-available/ /etc/uwsgi/apps-enabled/ /app  
COPY app.yml /etc/uwsgi/apps-available/  
COPY nginx.app /etc/nginx/sites-available/  
RUN rm /etc/nginx/sites-enabled/default  
RUN ln -s /etc/nginx/sites-available/nginx.app /etc/nginx/sites-enabled/  
RUN ln -s /etc/uwsgi/apps-available/app.yml /etc/uwsgi/apps-enabled/  
COPY app/application.py /app/  
COPY run.sh /tmp/  
  
EXPOSE 80  
CMD ["bash", "/tmp/run.sh"]  
  

