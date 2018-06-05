FROM python:2.7  
RUN pip install capstone pefile  
RUN git clone https://github.com/secretsquirrel/the-backdoor-factory.git  
  
WORKDIR the-backdoor-factory  
  
ENTRYPOINT ["./backdoor.py"]  

