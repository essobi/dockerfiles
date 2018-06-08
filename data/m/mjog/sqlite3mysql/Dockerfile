FROM python:3.5  
  
ADD ./sqlite3mysql.py /usr/bin/  
WORKDIR /usr/src  
RUN apt-get update \  
&& apt-get install -y sqlite \  
&& wget http://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-
python-2.1.3.tar.gz \  
&& tar xzvf mysql-connector-python-2.1.3.tar.gz \  
&& cd mysql-connector-python-2.1.3 \  
&& python setup.py install \  
&& chmod +x /usr/bin/sqlite3mysql.py  
  
CMD /usr/bin/sqlite3mysql.py  

