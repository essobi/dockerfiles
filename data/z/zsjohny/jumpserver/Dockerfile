FROM jumpserver/python:v3.6.1  
LABEL MAINTAINER Johny Zheng <shun.johny@gmail.com>  
  
COPY . /opt/jumpserver  
COPY utils/pip.conf /etc/pip.conf  
  
WORKDIR /opt/jumpserver  
  
RUN yum -y install epel-release  
RUN cd requirements && yum -y install $(cat rpm_requirements.txt)  
RUN pip install -r requirements.txt  
RUN yum clean all  
  
#RUN rm -f data/db.sqlite3  
RUN rm -r .git  
RUN rm -f config.py  
  
VOLUME /opt/jumpserver/data  
VOLUME /opt/jumpserver/logs  
  
RUN cp config_docker.py config.py  
  
EXPOSE 80  
EXPOSE 8080  
CMD cd utils && sh make_migrations.sh && sh init_db.sh && cd .. && python
run_server.py  

