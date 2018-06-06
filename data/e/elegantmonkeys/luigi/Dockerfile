FROM python:3.6.3  
RUN pip install 'luigi==2.7.1' 'sqlalchemy==1.1.15' 'psycopg2==2.7.3.2'  
RUN mkdir /etc/luigi && chmod -R a+rw /etc/luigi  
  
EXPOSE 8082  
CMD luigid  

