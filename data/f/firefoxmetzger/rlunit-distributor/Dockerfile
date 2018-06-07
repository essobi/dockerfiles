FROM python:2.7  
# install dependancies  
RUN apt-get update && \  
apt-get install libmysqlclient-dev -y  
ADD /RLUnit/distributor/Requirements.txt .  
RUN pip install -r Requirements.txt && rm Requirements.txt  
  
# Install RLUnit_database  
WORKDIR /RLUnit_database_install  
COPY database/ .  
RUN python setup.py install && cd .. && rm -rf /RLUnit_database_install  
  
# Base config  
ENV LOGGING_LEVEL=INFO  
ENV TASK_ADDRESS=tcp://*:5000  
ENV RESCHEDULE_TIME=120  
# The actual container files  
WORKDIR /app  
COPY RLUnit/distributor /app  
  
ENTRYPOINT ["python", "distributor.py"]  

