#from official python 2.7 docker build  
FROM python:2  
#Set working directory to app to run commands  
WORKDIR /app  
  
#Add requirements file before install requirements  
COPY requirements_ubertool.txt ./requirements_ubertool.txt  
  
#Install requirements, including nose2  
RUN pip install -r requirements_ubertool.txt  

