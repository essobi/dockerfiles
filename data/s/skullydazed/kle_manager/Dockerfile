FROM python:3.6  
MAINTAINER Zach White <skullydazed@gmail.com>  
EXPOSE 5000  
ADD web.py requirements.txt setup.py /kle_manager/  
ADD static/css/* /kle_manager/static/css/  
ADD templates/* /kle_manager/templates/  
WORKDIR /kle_manager  
RUN pip3 install git+git://github.com/skullydazed/kle2xy.git@master  
RUN pip3 install git+git://github.com/skullydazed/kle2svg.git@master  
RUN pip3 install -r requirements.txt  
ENV LC_ALL=C.UTF-8  
ENV LANG=C.UTF-8  
CMD gunicorn -w 8 -b 0.0.0.0:5000 --max-requests 1000 --max-requests-jitter
100 -t 60 web:app  

