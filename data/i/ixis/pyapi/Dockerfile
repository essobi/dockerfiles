FROM alpine  
RUN apk update && apk add py-pip unzip wget  
RUN pip install flask flask-restful requests flask-mysql boto3  
RUN wget http://cdn.mysql.com/Downloads/Connector-Python/mysql-connector-
python-2.0.4.zip#md5=3df394d89300db95163f17c843ef49df  
RUN unzip mysql-connector-python-2.0.4.zip && cd mysql-connector-python-2.0.4
&& python setup.py install  

