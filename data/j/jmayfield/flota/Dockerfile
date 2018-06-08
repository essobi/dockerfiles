FROM jmayfield/shellish  
  
RUN wget https://get.docker.com/builds/Linux/x86_64/docker-1.10.3 \  
-O /usr/bin/docker && \  
chmod +x /usr/bin/docker  
COPY requirements.txt /  
RUN pip install -r /requirements.txt  
COPY . /package  
RUN cd /package && python ./setup.py install  
ENTRYPOINT ["flota"]  

