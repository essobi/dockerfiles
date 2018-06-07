FROM frolvlad/alpine-python3  
MAINTAINER Alexandre Andrade <kaniabi@gmail.com>  
  
ENV WORKDIR="/srv" APPDIR="/app" ERR_USER="err"  
WORKDIR $WORKDIR  
  
RUN apk add --no-cache git py-cffi bash && \  
apk add --no-cache --virtual=build-dependencies gcc python3-dev musl-dev
libffi-dev openssl-dev && \  
pip3 install --upgrade pip && \  
pip3 install virtualenv  
  
RUN mkdir $WORKDIR/data $WORKDIR/plugins $WORKDIR/errbackends $APPDIR  
  
COPY requirements.txt $APPDIR/requirements.txt  
RUN virtualenv --system-site-packages -p python3 $APPDIR/venv && \  
$APPDIR/venv/bin/pip3 install --no-cache-dir -r $APPDIR/requirements.txt && \  
apk del build-dependencies  
  
EXPOSE 3141 3142  
VOLUME ["/srv"]  
  
COPY config.py $APPDIR/config.py  
COPY run.sh $APPDIR/venv/bin/run.sh  
CMD ["/app/venv/bin/run.sh"]  

