FROM python:2.7  
  
ENV \  
CUISINE_VERSION=0.7.13 \  
FABRIC_VERSION=1.11.1  
  
RUN apt-get update \  
&& apt-get install -y rsync  
RUN pip install \  
fabric==$FABRIC_VERSION \  
cuisine==$CUISINE_VERSION  
  
# install ipython for tab completion  
RUN pip install ipython  
  
  
WORKDIR /app  
  
#ENTRYPOINT ["fab"]  
# Add script that handles entrypoint commands  
ADD startup.py /root/startup.py  
RUN chmod +x /root/startup.py  
  
# Register our entry point script handler as the Docker Entrypoint  
ENTRYPOINT ["python","/root/startup.py"]

