FROM ubuntu:xenial  
  
RUN apt-get -y update && apt-get install -y python-pip  
RUN apt-get install -y python-dev libxml2-dev libxslt1-dev zlib1g-dev  
RUN apt-get install -y python-setuptools  
RUN apt-get install -y python-openssl  
  
RUN easy_install lxml  
  
ADD requirements.txt /  
RUN pip install -r requirements.txt  
  
ADD database_setup.py /  
CMD python database_setup.py  
  
ADD MITscraper /MITscraper  
ADD project.py /  
ADD static /static  
ADD templates /templates  
ADD grading.py /  
CMD wget http://jswebdev.atspace.cc/static/client_secrets.json  
CMD python project.py  

