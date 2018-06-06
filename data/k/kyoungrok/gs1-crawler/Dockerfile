FROM continuumio/miniconda  
MAINTAINER kyoungrok.jang@gmail.com  
  
ENV PYTHONUNBUFFERED 1  
# install dependencies  
RUN conda install psycopg2 scrapy sqlalchemy && pip install elasticsearch pytz
pymongo scrapy-splash  
  
# copy crawler code  
COPY code /code  
RUN chmod -R +x /code  
WORKDIR /code  
  
# entrypoint  
CMD ["bash", "/code/run-crawlers.sh"]  

