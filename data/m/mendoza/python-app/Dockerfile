# Comment for update deploy  
FROM python:2.7  
MAINTAINER mendozaene@gmail.com  
WORKDIR /app  
RUN apt-get update && apt-get install -y wget unzip  
RUN wget https://github.com/platzi/platzidocker/archive/master.zip  
RUN unzip master.zip  
RUN pip install -r platzidocker-master/app/requirements.txt  
CMD python platzidocker-master/app/app.py  
EXPOSE 5000  

