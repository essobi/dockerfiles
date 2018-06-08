FROM ubuntu  
ENV GIT_REV_TESTBED_DEPLOY develop  
RUN apt-get update && apt-get -y install python-pip python-dev \  
libmysqlclient-dev libpq-dev \  
libxml2-dev libxslt1-dev git \  
libffi-dev zip python-mysqldb netcat  
RUN git clone https://github.com/telefonicaid/fiware-testbed-deploy/
/home/ubuntu/fiware-testbed-deploy/  
WORKDIR /home/ubuntu/fiware-testbed-deploy/  
RUN git checkout ${GIT_REV_TESTBED_DEPLOY}  
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt  
RUN mkdir /root/.ssh  
COPY start.sh /home/ubuntu/fiware-testbed-deploy/start.sh  
CMD ./start.sh  

