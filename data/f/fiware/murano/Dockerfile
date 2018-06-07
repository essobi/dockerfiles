FROM ubuntu  
ENV GIT_REV_MURANO stable/newton  
RUN apt-get update && apt-get -y install python-pip python-dev \  
libmysqlclient-dev libpq-dev \  
libxml2-dev libxslt1-dev git \  
libffi-dev zip python-mysqldb netcat  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-server  
RUN pip install tox; git clone https://github.com/openstack/murano
/opt/murano/  
WORKDIR /opt/murano  
RUN git checkout ${GIT_REV_MURANO}  
COPY murano.conf /opt/murano/etc/murano/murano.conf  
COPY netconfig.yaml /opt/murano/etc/murano/netconfig.yaml  
COPY start.sh /opt/murano/start.sh  
COPY *.yaml /etc/murano/class-configs/  
EXPOSE 8082  
COPY meta /opt/murano/meta2  
CMD ./start.sh  

