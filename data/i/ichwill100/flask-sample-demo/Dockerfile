FROM ichwill100/flask-sample-demo:latest  
  
MAINTAINER Your Name "saul.vaca@amaris.com"  
RUN apt-get update -y && \  
apt-get install -y python-pip python-dev build-essential  
  
# We copy just the requirements.txt first to leverage Docker cache  
COPY ./requirements.txt /app/requirements.txt  
  
WORKDIR /app  
  
RUN pip install --upgrade pip  
  
RUN pip install -r requirements.txt  
  
COPY . /app  
  
EXPOSE 5000  
#RUN export FLASK_APP=app.py  
ENTRYPOINT [ "python" ]  
  
CMD [ "hello.py" ]  

