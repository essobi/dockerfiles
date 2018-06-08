FROM andyfangdz/alpine-glibc-python  
ENV PYTHONUNBUFFERED 1  
ENV ISDOCKERDEV True  
RUN apk add --no-cache postgresql-dev build-base python-dev libcurl curl-dev
libffi-dev  
RUN apk add --no-cache bash git nginx uwsgi uwsgi-python py-pip linux-headers
\  
&& pip install --upgrade pip \  
&& pip install flask  
RUN mkdir /requirements  
WORKDIR /requirements  
ADD requirements.txt /requirements/  
RUN pip install -r requirements.txt  

