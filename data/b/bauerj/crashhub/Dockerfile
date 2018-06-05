FROM python:3  
LABEL maintainer="Johann Bauer <bauerj@bauerj.eu>"  
  
COPY . /app  
RUN python /app/setup.py install  
RUN pip install uwsgi PyMySQL  
RUN useradd crashhub  
  
USER crashhub  
  
WORKDIR /app  
  
CMD uwsgi --socket 0.0.0.0:3031 --processes 2 --threads 2 --master --wsgi-file
/app/crashhub.py --callable app  

