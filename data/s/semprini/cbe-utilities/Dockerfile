# Start with a Python image.  
FROM python:latest  
  
# Set default required environment variables  
ENV PYTHONUNBUFFERED 1  
ENV DBENGINE sqlite3  
ENV DBNAME /code/dblocal.sqlite3  
ENV DBHOST None  
ENV DBPORT None  
ENV DBUSER None  
ENV DBPASSWORD None  
ENV SUNAME super  
ENV SUEMAIL super@super.com  
ENV SUPASS super  
  
# Install some necessary things.  
RUN apt-get update  
RUN apt-get install -y swig libssl-dev dpkg-dev netcat libmysqlclient-dev  
  
# Copy all our files into the image.  
RUN git clone https://github.com/Semprini/cbe-utilities.git /code  
WORKDIR /code  
  
# Install our requirements.  
RUN pip install -U pip  
RUN pip install -Ur requirements.txt  
RUN pip install uwsgi mysqlclient psycopg2  
  
# Collect our static media  
RUN python manage.py collectstatic --noinput  
  
# Specify the command to run when the image is run.  
RUN ["chmod", "+x", "/code/manage_run.sh"]  
RUN ["chmod", "+x", "/code/manage.py"]  
CMD ["/code/manage_run.sh"]  

