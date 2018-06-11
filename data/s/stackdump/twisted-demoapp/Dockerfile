FROM python:2.7.12  
ENV PROJECT_VERSION=0.1.0  
RUN mkdir -p /opt/poc-demoapp  
  
COPY requirements.txt /opt/poc-demoapp/  
WORKDIR /opt/poc-demoapp  
  
RUN pip install -r requirements.txt  
  
COPY . /opt/poc-demoapp/  
  
EXPOSE 8080  
VOLUME ["/opt/workspace", "/data"]  
  
ENTRYPOINT ["/opt/poc-demoapp/entry.sh"]  

