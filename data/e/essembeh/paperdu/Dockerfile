FROM debian:stable  
MAINTAINER Sébastien M-B <essembeh@gmail.com>  
  
## Repositories  
ADD sources.list /etc/apt/  
RUN apt-get update  
  
## UTF8 stuff  
RUN apt-get install -qy locales && apt-get clean  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
## Project dependencies  
RUN apt-get install -qy git python3 python3-pip python-virtualenv  
  
## Project  
RUN git clone https://github.com/essembeh/paperdu  
WORKDIR /paperdu  
RUN pip install -r requirements/base.txt  
RUN python manage.py syncdb --migrate --noinput  
  
## Server  
EXPOSE 8000  
ENTRYPOINT python manage.py createsuperuser --email=demo@example.org && python
manage.py runserver 0.0.0.0:8000  

