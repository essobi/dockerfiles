FROM centos:centos7  
  
# Add your app folder  
#ADD ./myapp /code  
#WORKDIR /code  
RUN yum -y update; yum clean all  
RUN yum -y install epel-release; yum clean all  
RUN yum -y install python-pip; yum clean all  
RUN yum -y install http://yum.postgresql.org/9.4/redhat/rhel-7.2-x86_64/pgdg-
redhat94-9.4-2.noarch.rpm; yum clean all  
RUN yum -y install git gcc geos postgresql94 postgresql94-devel libxml2-devel
libjpeg-turbo-devel libxslt-devel npm python-devel; yum clean all  
RUN pip install --upgrade pip;  
  
RUN npm install -g bower;  
RUN echo "{ \"allow_root\": true }" > ~/.bowerrc  
  
ENV PATH $PATH:/usr/pgsql-9.4/bin/  
  
# Add your python requirements  
#RUN pip install -r requirements.txt  
#CMD python app.py

