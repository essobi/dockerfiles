from python:2.7.14-jessie  
  
RUN apt-get update  
RUN git clone https://github.com/lorenzobenvenuti/cashbot /src  
WORKDIR /src  
RUN pip install -r requirements.txt  
  
CMD ["python", "cashbot.py", "/config/config.yml"]  

