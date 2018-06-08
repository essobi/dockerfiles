FROM python:3.5-onbuild  
MAINTAINER Vojta Bartos <hi@vojtech.me>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV SHELL /bin/bash  
ENV TERM xterm  
  
EXPOSE 5000  
CMD ["gunicorn", "-c", "gunicorn.py", "lift2fit:app"]  

