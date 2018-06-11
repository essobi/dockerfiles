FROM python:3.5  
ENV PYTHONUNBUFFERED 1  
COPY . /app  
  
# Requirements have to be pulled and installed here, otherwise caching won't
work  
COPY ./requirements /requirements  
RUN pip install -r /requirements/production.txt \  
&& groupadd -r django \  
&& useradd -r -g django django  
  
COPY ./compose/django/entrypoint.prod.sh /entrypoint.prod.sh  
RUN sed -i 's/\r//' /entrypoint.prod.sh \  
&& chmod +x /entrypoint.prod.sh \  
&& chown django /entrypoint.prod.sh  
  
WORKDIR /app  
  
CMD /entrypoint.prod.sh

