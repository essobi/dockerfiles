### Pull base repository ###  
FROM python:2.7  
FROM centos:centos7  
  
### Add maintainer ###  
MAINTAINER Paul Hitt <paulhitt@icloud.com>  
  
### Set environment variables ###  
ENV PYTHONUNBUFFERED 1  
  
### Add code to container ###  
RUN mkdir /code  
ADD . /code/  
  
### Install necessary software ###  
RUN yum install -y numpy scipy python-matplotlib ipython python-pandas sympy
python-nose git epel-release gcc openssl wget  
RUN yum install -y python-pip java-1.7.0-openjdk java-1.7.0-openjdk-devel  
RUN yum groupinstall -y "Development Tools"  
  
RUN pip install scikit-learn BeautifulSoup django-shop django-blog-zinnia
django-planet pillow pysolr simplejson django-bower haystack
djangorestframework  
  
RUN rpm -ivh
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.5.0.noarch.rpm  
  
RUN pip install -r /code/requirements.txt  
  
### Update the documentation ###  
RUN curl -X POST http://readthedocs.org/build/sharemyuniverse-zeus  
  
### Expose necessary ports ###  
EXPOSE 8000  
  
### Start the necessary services ###  
CMD /etc/init.d/elasticsearch start && python /code/manage.py runserver
0.0.0.0:8000  

