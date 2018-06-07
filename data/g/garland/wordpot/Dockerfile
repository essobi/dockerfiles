FROM ubuntu:16.04  
ADD ./ /opt/wordport  
  
RUN apt-get update  
RUN apt-get install -y python python-pip  
RUN pip install flask  
  
#ENTRYPOINT python /opt/wordport/wordpot.py  
#CMD python /opt/wordport/wordpot.py --host=0.0.0.0 --port=80  

