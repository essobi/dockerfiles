FROM python:3.5  
RUN apt-get update &&\  
apt-get install -y libmysqlclient-dev  
  
COPY . /usr/src/app  
  
WORKDIR /usr/src/app  
  
RUN pip install -r requirements.txt  
  
RUN python3 manage.py migrate --no-input &&\  
python3 manage.py collectstatic --no-input  
  
EXPOSE 8080  
ENV DJANGO_CONFIGURATION=Prod  
  
CMD ["./start.sh"]  

