FROM python:2.7  
LABEL maintainer "Martijn Pepping <martijn.pepping@automiq.nl>"  
  
RUN apt-get update && apt-get install unzip -y && \  
wget https://github.com/BenjV/autosub-bootstrapbill/archive/master.zip && \  
unzip master.zip -d /opt && rm master.zip && \  
pip install cheetah  
  
EXPOSE 9960  
WORKDIR /opt/autosub-bootstrapbill-master  
CMD ["python2", "AutoSub.py"]  

