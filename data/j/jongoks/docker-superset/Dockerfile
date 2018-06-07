FROM jongoks/docker-python3  
  
MAINTAINER Jongoks <jongoks@gmail.com>  
  
# Configure environment  
ENV LANG=C.UTF-8 \  
LC_ALL=C.UTF-8 \  
SUPERSET_HOME=/home/superset  
  
# Install  
RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev
python-pip libsasl2-dev libldap2-dev && \  
pip install superset==0.20.4 pymysql && \  
printf "admin\nadmin\nuser\nroot@localhost\nadmin\nadmin\n" | fabmanager
create-admin --app superset && \  
superset db upgrade && \  
superset load_examples && \  
superset init  
  
  
  
WORKDIR /home/superset  
EXPOSE 9999  
  
CMD bash -c "superset runserver -p 9999"  

