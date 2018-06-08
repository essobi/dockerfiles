FROM debian:8  
RUN apt-get update && apt-get install -y mysql-utilities  
ADD . /root/  
WORKDIR /root  
RUN chmod +x /root/migrate.sh  
RUN python ./setup.py build && python ./setup.py install  

