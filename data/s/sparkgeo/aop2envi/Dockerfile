FROM geodata/gdal  
  
USER root  
  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends git python-pip  
  
WORKDIR /app_src  
  
COPY requirements.txt requirements.txt  
  
RUN pip install -r requirements.txt  
  
COPY . /app_src  
  
CMD ["python", "app.py"]  

