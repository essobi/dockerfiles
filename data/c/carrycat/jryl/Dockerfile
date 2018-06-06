FROM python:3-slim  
ENV PYTHONUNBUFFERED 1  
RUN mkdir /code  
RUN apt-get update \  
&& apt-get install -y \  
binutils libproj-dev gdal-bin git gcc\  
&& rm -rf /var/lib/apt/lists/*  
WORKDIR /code  
ADD ./requirements.txt /code/  
#RUN pip install -U pip-tools  
RUN pip install -r requirements.txt -i
https://pypi.tuna.tsinghua.edu.cn/simple  
RUN pip --no-cache-dir install "git+https://github.com/DrChai/aliyun-openapi-
python-sdk.git#egg=aliyunsdkcore&subdirectory=aliyun-python-sdk-core-v3"  
COPY . /code/  
# RUN pip-compile requirements.in > requirements.txt  
RUN chmod 755 wait-for-it.sh  
RUN chmod 755 start-server.sh  
CMD [ "./wait-for-it.sh", "-t", "0", "127.0.0.1:5432", "--", "./start-
server.sh"]  
#CMD python manage.py runserver 0.0.0.0:8000  
EXPOSE 8000  
VOLUME ["/code/static", "/code/media"]  

