FROM firefoxmetzger/gym:latest  
ENV PYTHONPATH=$PYTHONPATH:/usr/local/gym  
  
# external dependancies  
RUN sudo apt-get update && \  
apt-get install libmysqlclient-dev -y  
WORKDIR /app  
COPY RLUnit/worker/Requirements.txt /app  
RUN pip install -r Requirements.txt && rm Requirements.txt  
  
# RLUnit-database  
WORKDIR /database  
COPY database/ .  
RUN python setup.py install && cd .. && rm -rf /database  
  
WORKDIR /app  
ENV LOGGING_LEVEL=INFO  
ENV QUEUE_ADDRESS=tcp://127.0.0.1:5000  
ENV HUB_ADDRESS=tcp://127.0.0.1:4444  
ENV DB_ADDRESS=mysql://root:password@127.0.0.1/reinforcement_learning  
ENV FORCE_INSERT=120  
COPY RLUnit/worker/ /app  
CMD ["python", "main.py"]  

