FROM python:3-alpine  
  
COPY configurator.py /src/  
COPY settings.conf /config/  
  
EXPOSE 3218  
VOLUME ["/config"]  
  
CMD ["python", "/src/configurator.py", "/config/settings.conf"]  

