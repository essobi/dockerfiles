FROM ubuntu:artful AS tipsi_base  
  
MAINTAINER Kirill Pinchuk <cybergrind@gmail.com>  
RUN echo '20 Feb 2018'  
  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
ENV LC_ALL C.UTF-8  
ENV SUPERVISOR_CONFIG supervisor-app.conf  
ENV LOG_DIR /var/log/tipsi  
ENV PYTHONPATH=.  
  
# Redefine next variables  
ENV CONTAINER_TYPE base_python  
ENV LOGSTASH_HOST localhost  
  
COPY base_python/install_basic_packages.sh .  
RUN ./install_basic_packages.sh  
  
COPY base_python/bootstrap/ /bootstrap  
WORKDIR /bootstrap  
RUN ./prepare_environment.py  
  
# setup supervisor  
# setup logdir and declare as volume  
# run default filebeat > logs from default log dir  
VOLUME $LOG_DIR  
VOLUME /filebeat  
CMD /bootstrap_env/bin/python /bootstrap/bootstrap.py  

