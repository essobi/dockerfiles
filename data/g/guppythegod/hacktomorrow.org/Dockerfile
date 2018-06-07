# PULLS IMAGE WITH PRECONFIGS  
FROM tiangolo/uwsgi-nginx-flask:python3.6  
# COPIES REQUIREMENTS TO TMP DIRECTORY IN CONTAINER  
COPY requirements.txt /tmp/  
  
# UPDATES PIP  
RUN pip install -U pip  
  
# INSTALLS THE REQUIREMENTS FILE  
RUN pip install -r /tmp/requirements.txt  
  
# COPIES APPLICATION FILES TO APP DIRECTORY IN CONTAINER  
COPY ./app /app  
  
# OPENS PORT 80 FOR INCOMING & OUTGOING  
# EXPOSE 80  
# RUNS THE SERVER FILE  
# CMD ["flask", "run"]  

