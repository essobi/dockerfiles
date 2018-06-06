FROM firefoxmetzger/rlunit-pipeline-base  
  
ENV WORKER_EVENT_ADDRESS=tcp://*:4000  
ENV PIPELINE_PUBLISHER_ADDRESS=tcp://*:5000  
WORKDIR /app  
COPY RLUnit/hub/main.py .  
  
ENTRYPOINT ["python","main.py"]  

