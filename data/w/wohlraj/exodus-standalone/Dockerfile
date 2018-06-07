FROM python:slim  
  
RUN apt update && apt install -y git  
RUN git clone https://github.com/Exodus-Privacy/exodus-standalone.git  
WORKDIR /exodus-standalone  
  
RUN pip install virtualenv  
RUN virtualenv venv -p python3  
  
RUN sed -i
's/androguard==3.1.0/https:\/\/github.com\/androguard\/androguard\/archive\/v3.1.0-pre.2.zip/'
requirements.txt  
RUN . venv/bin/activate && pip install -r requirements.txt  

