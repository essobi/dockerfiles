FROM python:2  
RUN pip install flask && \  
pip install flask_restful && \  
pip install pymongo && \  
pip install requests  
RUN mkdir -p codegladiator/dbCommunicator/logs  
VOLUME codegladiator  
COPY databaseCommunicator/ codegladiator/dbCommunicator/  
#VOLUME codegladiator  
# `mkdir /codegladiator/test`  
#CMD ["python","codegladiator/backend/databaseCommunicator/main.py"]  

