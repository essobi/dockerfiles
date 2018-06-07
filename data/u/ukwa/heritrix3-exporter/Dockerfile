FROM python:2.7  
# Install the monitor package:  
COPY . /monitor  
WORKDIR /monitor  
  
# Install  
RUN pip install --no-cache-dir -r requirements.txt  
RUN python setup.py install  
  
# Run the stats endpoint  
CMD ["python", "heritrix3_exporter.py"]  

