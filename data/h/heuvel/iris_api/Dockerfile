FROM buildo/docker-python2.7-scikit-learn  
  
RUN apt-get update && apt-get install -y wget  
  
# Install python packages  
RUN pip install --upgrade pip  
RUN pip install flask  
RUN pip install -U scikit-learn  
  
COPY api/* /opt/api/  
  
WORKDIR /opt/api  
  
CMD ["python", "app.py"]  
  

