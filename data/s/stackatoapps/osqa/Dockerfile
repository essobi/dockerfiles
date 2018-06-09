FROM ubuntu:12.04  
  
COPY . /src  
  
RUN cd /src && apt-get update && apt-get install -y python-dev && apt-get
install -y libmysqlclient-dev && apt-get install -y python-pip && pip install
-r requirements.txt  
  
CMD cd /src && python manage.py syncdb --all \--noinput && python manage.py
migrate forum --fake --noinput && python manage.py runserver 0.0.0.0:$PORT  

