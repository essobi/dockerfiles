FROM ubuntu:16.04  
#Layer for python and gdal support  
RUN apt-get update && apt-get install -y software-properties-common curl  
RUN add-apt-repository ppa:ubuntugis/ubuntugis-unstable && apt-get update  
RUN apt-get install -y python-pip libssl-dev libffi-dev python-gdal  
RUN rm -rf /var/lib/apt/lists/*  
#Begin of mandatory layers for Microsoft ODBC Driver 13 for Linux  
RUN apt-get update && apt-get install -y apt-transport-https wget  
RUN sh -c 'echo "deb [arch=amd64] https://apt-
mo.trafficmanager.net/repos/mssql-ubuntu-xenial-release/ xenial main" >
/etc/apt/sources.list.d/mssqlpreview.list'  
RUN apt-key adv --keyserver apt-mo.trafficmanager.net --recv-keys 417A0893  
RUN apt-get update -y  
RUN apt-get install -y libodbc1-utf16 unixodbc-utf16 unixodbc-dev-utf16  
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql  
#End of mandatory layers for Microsoft ODBC Driver 13 for Linux  
RUN apt-get remove -y curl  
#Layers for the django app  
RUN apt-get clean && apt-get update && apt-get install -y locales  
RUN locale-gen en_US.utf8 && update-locale  
COPY requirements.txt /code/requirements.txt  
WORKDIR /code  
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt  
#RUN mkdir /code  
COPY . /code/  
RUN python manage.py collectstatic --noinput  
#Layer for exposing the app through gunicorn  
EXPOSE 8002  
COPY entrypoint.sh /code/  
WORKDIR /code  
ENTRYPOINT ["sh", "entrypoint.sh"]  

