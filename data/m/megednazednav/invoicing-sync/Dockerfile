FROM python:3  
WORKDIR /app  
COPY requirements.txt /app  
RUN pip install -q -v -r requirements.txt  
COPY . /app  
CMD python -u main.py --noauth_local_webserver

