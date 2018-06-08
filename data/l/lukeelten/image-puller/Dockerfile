FROM python:alpine  
LABEL authors="Kévin Darcel <kevin.darcel@gmail.com>, Tobias Derksen
<t.derksen@gmx.de>"  
  
WORKDIR /usr/src/docker-image-updater  
  
COPY app.py requirements.txt /usr/src/docker-image-updater/  
  
RUN pip install --no-cache-dir -r requirements.txt && pip install --no-cache-
dir redis  
  
EXPOSE 8080  
STOPSIGNAL SIGTERM  
  
ENTRYPOINT ["python", "-u", "app.py"]  

