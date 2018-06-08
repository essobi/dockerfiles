FROM ubuntu:15.10  
# add unprivileged user  
RUN useradd -ms /bin/bash runner  
  
# install needed packages  
RUN apt-get -y update && apt-get -y install python python3 python3.5 git
python3-pip \  
postgresql-client sqlite3 libmysqlclient-dev python-dev libpq-dev  
  
# install tox  
RUN pip3 install tox  
  
# copy mailman configs  
COPY mysql.cfg postgres.cfg /home/runner/configs/  
RUN chown -R runner:runner /home/runner/configs  
  
# set working dir  
#USER runner  
#WORKDIR /home/runner  

