FROM python  
MAINTAINER Hayamatsu <contact@hayamatsu.fr>  
  
RUN pip install zerobin funcsigs && \  
mkdir -p /opt/0bin/data  
  
ADD settings.py /opt/0bin/settings.py  
EXPOSE 8080  
CMD ["zerobin", "--settings-file", "/opt/0bin/settings.py"]  
  

