FROM python:3.6-rc-alpine  
LABEL maintainer="knarfeh@outlook.com"  
  
# base pkgs  
RUN apk --update add --no-cache openssl ca-certificates postgresql-dev nginx
supervisor  
  
# build pkgs  
# Use uwsgi: http://note.qidong.name/2017/06/28/uwsgi-in-docker/  
RUN apk add gcc g++ python3-dev musl-dev make  
  
# dev pkgs  
RUN apk add curl  
  
COPY requirements /requirements  
RUN mkdir -p /var/log/eebook  
RUN pip3 install -U pip \  
&& pip install -i https://pypi.douban.com/simple -r requirements/dev.txt \  
&& pip install gunicorn==19.6.0  
EXPOSE 80  
COPY . /src/  
WORKDIR /src  
  
CMD chmod u+x /src/run.sh  
CMD ["/src/run.sh"]

