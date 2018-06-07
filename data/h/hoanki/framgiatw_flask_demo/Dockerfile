FROM ubuntu:16.04  
MAINTAINER Group_4 <FramgiaTranningWorkShop>  
  
RUN DEBIAN_FRONTEND=noninteractive  
  
RUN apt update  
  
# Create virtualenv folder and coppy all to it  
ADD . /venv  
  
WORKDIR /venv  
  
# Instal python  
RUN apt-get install -y python python-dev python-pip python-virtualenv \  
&& pip install --upgrade pip  
  
# Instal required packages listed in requirements.txt  
COPY requirements.txt /venv  
RUN apt-get install -y libmysqlclient-dev # Install for MySQL-python in
requirements.txt  
RUN pip install -r requirements.txt  
  
# Install "software-properties-common" (for the "add-apt-repository")  
RUN apt-get update && apt-get install -y \  
software-properties-common \  
supervisor  
# Install Mysql  
RUN echo "mysql-server mysql-server/root_password password root" | debconf-
set-selections \  
&& echo "mysql-server mysql-server/root_password_again password root" |
debconf-set-selections \  
&& apt-get install -y mysql-server  
  
# Run migration with alembic  
# Start by installing the module  
RUN pip install alembic  
# Create your migrations environment. We use "generic" which is a single
database setup  
# RUN alembic init --template generic alembic  
# Edit alembic.ini with your connection details  
# RUN sed -i -e 's/sqlalchemy.url.*/sqlalchemy.url =
mysql:\/\/root:root@localhost\/framgiatw/g' alembic.ini  
EXPOSE 5000  
RUN chmod a+x /venv/*  
ENTRYPOINT ["/venv/entrypoint.sh"]  

