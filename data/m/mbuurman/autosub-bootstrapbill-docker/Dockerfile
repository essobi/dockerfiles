FROM python:2.7  
RUN apt-get update && apt-get install unzip nano git -y  
  
RUN wget https://github.com/BenjV/autosub/archive/master.zip && \  
unzip master.zip -d /opt && \  
rm master.zip  
  
RUN pip install cheetah  
  
EXPOSE 8083  
EXPOSE 9960  
WORKDIR /opt/autosub-master  
  
CMD ["python2", "AutoSub.py"]  

