FROM python:2.7-slim  
  
LABEL AUTHOR="Ravindra Bhadti"  
  
RUN pip install --upgrade pip setuptools && \  
pip install django django-lint  
  
ENTRYPOINT ["django-lint"]

