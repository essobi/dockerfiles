FROM python:3  
WORKDIR /opt  
  
RUN pip install flask requests wasp-eureka rivescript python-jose wordfilter
pytest pytest-allure-adaptor  
  
COPY LogicaCha.py /opt/  
COPY device.rive /opt/  
COPY chatbot.rive /opt/  
COPY chatController.py /opt/  
COPY register.py /opt/  
COPY runAll.py /opt/  
COPY chatbot.json /opt/  
  
EXPOSE 5002  
CMD python3 ./runAll.py  

