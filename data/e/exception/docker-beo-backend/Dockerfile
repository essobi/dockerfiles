FROM ubuntu:16.04  
RUN echo "A2"  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y python3-pip python-pip python-dev build-essential git
libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev
tcl8.6-dev tk8.6-dev python-tk vim  
RUN pip install --upgrade pip  
RUN echo "C1"  
RUN git clone https://github.com/ppschweiz/python-civicrm  
RUN cd python-civicrm && python3 setup.py install  
RUN echo "B10"  
RUN git clone -b 17.04 https://github.com/ppschweiz/ekklesia.git  
RUN cd ekklesia && make install  
RUN git clone https://github.com/ppschweiz/python-civi  
RUN pip install pymysql psycopg2  
COPY run.sh /run.sh  
COPY run-once.sh /run-once.sh  
COPY push.sh /push.sh  
COPY init.sh /init.sh  
COPY static.sh /static.sh  
COPY ekklesia.ini /ekklesia.ini  
CMD ["/run.sh"]  

