FROM python:2.7  
  
RUN apt-get update && \  
apt-get install -y groff && \  
pip uninstall -y virtualenv && \  
pip install awscli==1.7.3 && \  
apt-get -y autoremove && \  
apt-get -y autoclean  
  
ENTRYPOINT ["aws"]  
CMD ["help"]

