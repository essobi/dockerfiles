FROM ubuntu:14.04  
MAINTAINER Mateo <mateo@paybook.me>  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-all python-pip  
RUN apt-get install -y git  
RUN apt-get update  
RUN apt-get install -y nodejs  
RUN apt-get install -y npm  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install -g bower  
RUN cd /tmp  
RUN git clone https://github.com/Paybook/lite-python.git  
ADD ./lite-python/requirements.txt /tmp/requirements.txt  
RUN pip install -qr /tmp/requirements.txt  
RUN mv lite-python /opt/lite-python  
WORKDIR /opt/lite-python  
EXPOSE 5000  
#ENTRYPOINT ["/usr/bin/python /opt/lite-python/main.py"]  
CMD ["python", "main.py"]  

