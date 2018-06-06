FROM frolvlad/alpine-python3  
  
COPY requirements.txt /opt/requirements.txt  
RUN pip install -r /opt/requirements.txt  
  
COPY . /opt/  
WORKDIR /opt/  
USER nobody  
  
CMD FLASK_APP=freeipa_change_password_service.py flask run --host 0.0.0.0
--port 5000  

