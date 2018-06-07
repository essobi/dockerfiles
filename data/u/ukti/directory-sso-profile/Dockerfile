FROM python:3.5  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY requirements.txt /usr/src/app/  
# Different src directory for pip to prevent 'pip install -e' packages to be
installed in /usr/src/app/  
RUN pip install --no-cache-dir -r requirements.txt --src /usr/local/src  
  
COPY . /usr/src/app  
  
CMD ["/usr/src/app/docker/cmd-webserver.sh"]  
  
EXPOSE 8000  

