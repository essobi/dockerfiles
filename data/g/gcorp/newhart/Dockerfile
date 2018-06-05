FROM alpine:3.7  
MAINTAINER xander@gahancorporation.com  
RUN apk update  
RUN apk add python3; ln -sf /usr/bin/python3 /usr/bin/python  
RUN apk add python3-dev  
RUN apk add wget  
RUN wget https://bootstrap.pypa.io/get-pip.py; python get-pip.py; rm get-
pip.py; ln -sf /usr/bin/pip3 /usr/bin/pip  
RUN apk add git  
RUN apk add postgresql  
RUN apk add postgresql-dev  
RUN apk add build-base  
RUN wget https://codeclimate.com/downloads/test-reporter/test-reporter-latest-
linux-amd64 -O /usr/bin/cc-test-reporter; chmod +x /usr/bin/cc-test-reporter  
RUN git clone https://github.com/gahan-corporation/newhart.git /srv/newhart  
WORKDIR /srv/newhart  
RUN git checkout v0.0.1  
ENV DJANGO_SETTINGS_MODULE newhart.settings  
ENV CODACY_PROJECT_TOKEN 61a8f55ecf394f68a0b4c2d1c0f14d8a  
ENV CC_TEST_REPORTER_ID
82428da430f003a16e79bb4da19d1f4b045712dee9c8dff967462c6580a1b567  
RUN pip install -r /srv/newhart/.requirements  
EXPOSE 8000  
CMD newhart/manage.py runserver 0.0.0.0:8000  

