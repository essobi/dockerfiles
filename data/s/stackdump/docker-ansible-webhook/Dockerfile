FROM python:2.7  
  
RUN useradd --uid 1000 -d /opt/ims ims && \  
echo "ims ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
RUN apt-get update && \  
apt-get install -y \  
wget curl git vim tig screen tree  
  
ENV PROJECT_VERSION=0.0.2  
  
RUN mkdir /opt/app && chown ims:ims /opt/app  
  
COPY requirements.txt /opt/app/  
WORKDIR /opt/app  
  
RUN pip install -r requirements.txt  
  
COPY . /opt/app/  
RUN chown -R ims:ims /opt/app  
USER ims  
  
EXPOSE 8080  
VOLUME ["/home/ims", "/opt/ims"]  
  
CMD cptwebhook -k bee72934-109f-11e6-9000-7b065b4a6abb -p 8080 ./deploy.sh  

