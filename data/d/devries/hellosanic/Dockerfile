FROM python:3.6  
MAINTAINER Christopher De Vries <devries@idolstarastronomer.com>  
  
RUN pip install sanic jinja2  
  
RUN groupadd -g 2000 apprunner  
RUN useradd -u 2000 -g apprunner -d / -s /usr/sbin/nologin -c "Docker image
user" apprunner  
  
COPY main_app.py /app/  
COPY templates /app/templates  
WORKDIR /app  
RUN chown -R apprunner:apprunner /app  
  
EXPOSE 8080  
USER apprunner  
  
CMD ["python","-m","sanic","main_app.app","--host","0.0.0.0","--port","8080","
--workers","4"]  
  

