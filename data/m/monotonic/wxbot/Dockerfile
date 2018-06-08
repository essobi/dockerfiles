FROM python:3  
RUN mkdir /code/  
WORKDIR /code/  
  
ADD requirements.txt .  
  
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple/  
  
VOLUME /bots  
  
ADD . /code/  
  
ENV TZ="Asia/Shanghai"  
ENV BOT_SENTRY_DSN="" BOT_SECRET_KEY="" BOT_JS_VERSION=""  
ENV BOT_QINIU_ACCESS_KEY="" BOT_QINIU_SECRET_KEY="" BOT_QINIU_BUCKET=""
BOT_QINIU_ROOT=""  
ENV PYTHONUNBUFFERED=1  
EXPOSE 5000  
ENTRYPOINT ["gunicorn", "--access-logfile", "/tmp/gunicorn.log", "-b",
"0.0.0.0:5000", "-k", "gevent", "wxbot:app"]  

