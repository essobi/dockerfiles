FROM python:3.5.2-alpine  
LABEL maintainer="jesseadametz@gmail.com"  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY index.html life.md ./  
  
EXPOSE 8080  
CMD ["python", "-m", "http.server", "8080"]  

