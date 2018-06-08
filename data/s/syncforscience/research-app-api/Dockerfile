FROM python:3-onbuild  
MAINTAINER Josh Mandel  
  
# Configure the app  
ENV FLASK_APP "/usr/src/app/app.py"  
ENV AUTH_USERNAME "s4s-app"  
ENV AUTH_PASSWORD "s4s-app-secret"  
WORKDIR /usr/src/app  
  
ENTRYPOINT ["flask"]  
CMD ["run", "--host", "0.0.0.0"]  

