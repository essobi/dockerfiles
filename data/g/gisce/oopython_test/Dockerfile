FROM python:2.7  
MAINTAINER GISCE-TI, S.L <devel@gisce.net>  
  
RUN apt-get update  
RUN apt-get install -y freetds-common freetds-dev  
RUN apt-get install -y libgdal-dev  
  
RUN virtualenv /home/erp  
  
ENV LIB /home/erp/src  
RUN mkdir -p ${LIB}  
  
RUN /home/erp/bin/pip install --upgrade pip  
RUN /home/erp/bin/pip install cython lxml psycopg2 egenix-mx-base babel \  
vatnumber reportlab==3.0  
  
ADD sitecustomize.py /home/erp/lib/python2.7/sitecustomize.py  
  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

