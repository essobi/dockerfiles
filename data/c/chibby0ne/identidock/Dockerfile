FROM python:3.4  
  
# Creates the uwsgi user and group in an normal Unix fashin  
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi  
RUN pip install FLask==0.10.1 uWSGI==2.0.8 requests==2.5.1 redis==2.10.3  
WORKDIR /app  
COPY app /app  
COPY cmd.sh /  
  
# Uses the EXPOSE instruction to declare the ports accesible to the host and
other containers  
EXPOSE 9090 9091  
  
# Sets the user for all the following lines (including CMD and ENTRYPOINT) to
be uwsgi  
USER uwsgi  
  
# New command to run uWSGI. Tell uSWGI to tstart an http server listing on
port 9090 urnning the app application from /app/indentidock.py. It starts a
stats sever on port 9091. We could alternatively have overriden the CMD via
the docker run command  
# CMD ["uwsgi", "--http", "0.0.0.0:9090", "--wsgi-file", "/app/identidock.py",
"--callable", "app", "--stats", "0.0.0.0:9091"]  
  
CMD ["/cmd.sh"]  

