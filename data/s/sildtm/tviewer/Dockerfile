FROM python:3.5.2-alpine  
  
ENV PROJECT_ROOT_DIR /opt/tviewer  
ENV DATA_DIR /var/lib/tviewer  
ENV LOG_DIR /var/log/tviewer  
  
RUN pip install Django  
  
COPY tviewer_py ${PROJECT_ROOT_DIR}/tviewer_py  
COPY webapp ${PROJECT_ROOT_DIR}/webapp  
COPY manage.py ${PROJECT_ROOT_DIR}/  
COPY docker_content/entrypoint.sh /  
  
VOLUME ["${DATA_DIR}", "${LOG_DIR}"]  
EXPOSE 80  
ENTRYPOINT [ "/bin/sh", "entrypoint.sh" ]  
  

