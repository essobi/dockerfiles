FROM openmatchmaking/docker-base-python-image:3.6  
COPY requirements.txt /requirements.txt  
RUN pip install -r requirements.txt  
  
COPY game-servers-pool /app  
WORKDIR /app  

