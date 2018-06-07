FROM python:2.7  
#Install Required Applications  
RUN apt-get update && apt-get install -y unixodbc unixodbc-dev tdsodbc iodbc
nano freetds-bin python2.7 python-pip python-dev  
  
#Copy over the DJANGO Site Code  
RUN mkdir /site  
WORKDIR /site  
ADD site/. /site/  
RUN pip install -r requirements.txt  
  
#Copy configurations for ODBC Connections  
ADD /conf/odbcinst.ini /etc/  
ADD /conf/odbc.ini /etc/  
ADD /conf/freetds.conf /etc/freetds/freetds.conf  
  
EXPOSE 8000  
CMD ["python", "/site/manage.py", "runserver", "0.0.0.0:8000"]  

