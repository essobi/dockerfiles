FROM python:3.5  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY requirements.txt /usr/src/app/  
# Use pip v9 as v10 introduced breaking changes see ED-4130  
RUN pip install --upgrade pip==9.0.1  
# Different src directory for pip to prevent 'pip install -e' packages to be
installed in /usr/src/app/  
RUN pip install --no-cache-dir -r requirements.txt --src /usr/local/src  
  
COPY . /usr/src/app  
  
# Install dockerize https://github.com/jwilder/dockerize  
ENV DOCKERIZE_VERSION v0.5.0  
RUN wget -q
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
CMD ["/usr/src/app/docker/cmd-webserver.sh"]  
  
EXPOSE 8000  

