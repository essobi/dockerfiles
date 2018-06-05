FROM ubuntu  
RUN apt-get update  
RUN apt-get -y install python-dev \  
libpq-dev libmysqlclient-dev libpq-dev \  
git curl netcat libffi-dev zip python-mysqldb \  
supervisor python-clips build-essential gcc  
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"  
RUN python get-pip.py  
RUN git clone https://github.com/telefonicaid/fiware-facts /opt/fiware-facts  
WORKDIR /opt/fiware-facts  
RUN mkdir /etc/fiware.d/  
RUN mkdir /var/log/fiware-facts  
RUN pip install -r requirements.txt  
RUN pip install MySQL-python  
COPY config.py facts/config.py  
COPY fiware-facts.cfg /etc/fiware.d/fiware-facts.cfg  
COPY start.sh start.sh  
COPY config.py facts_conf/config.py  
CMD ./start.sh  

