FROM python:3.6-alpine  
WORKDIR /app  
COPY . /app  
EXPOSE 8000  
RUN mkdir -p /database /static && \  
pip install -U pip setuptools && \  
pip install -r requirements.txt && \  
sed -i -e 's/^DEBUG = True/DEBUG = False/' /app/superlists/settings.py && \  
sed -i -e 's/^ALLOWED_HOSTS .*/ALLOWED_HOSTS = ["127.0.0.1", "localhost",
"superlists.myk8s.net"]/' /app/superlists/settings.py  
CMD python manage.py serve.py  

