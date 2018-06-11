FROM python:3.6-alpine3.6  
RUN pip install pymongo  
COPY mongo_rs_controller.py /usr/local/bin/mongo_rs_controller.py  
  
ENTRYPOINT ["/usr/local/bin/mongo_rs_controller.py"]  

