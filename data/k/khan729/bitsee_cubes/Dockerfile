FROM python:3  
ENV PYTHONUNBUFFERED 1  
WORKDIR /root/src  
  
RUN pip install pika  
  
RUN pip install PyMySQL  
  
RUN pip install pysnowflake  
  
RUN pip install redis  
  
RUN pip install sqlalchemy -i https://mirrors.aliyun.com/pypi/simple  
  
RUN pip install click  
  
RUN pip install flask  
  
RUN pip install uwsgi  
  
RUN pip install cryptography  
  
RUN pip install pyjwt  
  
COPY . /root  
  
RUN echo "Asia/Shanghai" > /etc/timezone  
RUN dpkg-reconfigure -f noninteractive tzdata  
  
RUN pwd  
  
RUN /bin/sh -c 'cd /root/cubes && python setup.py bdist_egg && easy_install
./dist/cubes-1.1-py3.6.egg'  
  
CMD [ "uwsgi","config.ini" ]  

