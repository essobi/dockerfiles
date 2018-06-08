# Use current version of Ubuntu  
FROM ubuntu:latest  
  
# Get latest version of Python and Pip  
RUN apt-get update -y  
RUN apt-get install -y python-pip python-dev build-essential  
RUN apt-get install libpq-dev -y  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Bundle app source  
COPY /app/app.py /usr/src/app  
COPY /app/config.py /usr/src/app  
COPY /app/helpers.py /usr/src/app  
COPY /app/manage.py /usr/src/app  
COPY /app/models.py /usr/src/app  
COPY /app/health_prediction.pkl /usr/src/app  
COPY /app/migrations /usr/src/app  
COPY requirements.txt /usr/src/app  
COPY Dockerfile /usr/src/app  
  
# Install app dependencies  
RUN pip install -r requirements.txt  
  
# Expose port  
EXPOSE 5000  
# Use Dockerize to stall pip install  
RUN apt-get update && apt-get install -y wget  
  
ENV DOCKERIZE_VERSION v0.2.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
CMD dockerize -wait http://predictionServiceDB:5432 -timeout 360s  
CMD echo "source `which activate.sh`" >> ~/.bashrc  
CMD source ~/.bashrc  
CMD cd ..  
CMD cd app  
CMD python app.py  
# CMD python manage.py db init  
# CMD python manage.py db migrate  
# CMD python manage.py db upgrade  

