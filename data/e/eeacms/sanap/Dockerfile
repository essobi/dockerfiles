FROM python:2.7  
ENV SECRETY_KEY="changeme"  
ENV SENTRY_DSN=""  
ENV HOSTNAME=""  
RUN apt-get update && apt-get install -y libldap2-dev libsasl2-dev wkhtmltopdf  
  
RUN mkdir -p /app/instance/files  
COPY sanap /app/sanap  
COPY libs /app/libs  
COPY settings.py.docker /app/instance/settings.py  
COPY requirements.txt /app/requirements.txt  
WORKDIR /app  
RUN pip install -r requirements.txt  
  
EXPOSE 5000  
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "sanap.manage:app"]  
  

