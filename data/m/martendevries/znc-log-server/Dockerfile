FROM alpine  
  
RUN apk add --no-cache uwsgi uwsgi-python3 py3-flask py3-jinja2  
ADD src /src  
WORKDIR /src  
RUN echo "import os; LOG_PATH = '/log'; CHANNELS =
os.environ['CHANNELS'].split(';')" > config.py  
CMD uwsgi --plugin python3 --socket :3031 --manage-script-name --mount
$MOUNT_POINT=server:app  

