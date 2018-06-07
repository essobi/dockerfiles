  
FROM alpine:3.7  
  
RUN set -x \  
&& apk add --no-cache \  
coreutils \  
ca-certificates \  
duplicity \  
openssh \  
openssl \  
rsync \  
lftp \  
mailx \  
curl \  
bash  
  
ADD https://github.com/zertrin/duplicity-backup.sh/raw/dev/duplicity-backup.sh
/usr/local/bin/  
COPY entrypoint.sh /home/duplicity/entrypoint.sh  
  
ENV HOME=/home/duplicity  
  
RUN adduser -D -u 1896 duplicity \  
&& mkdir -p ${HOME}/.cache/duplicity \  
&& mkdir -p ${HOME}/.gnupg \  
&& chmod -R go+rwx ${HOME}/ \  
&& mkdir -p /var/log/duplicity \  
&& chmod -R go+rw /var/log/duplicity/ \  
&& chmod +rx /usr/local/bin/duplicity-backup.sh \  
&& chmod +rx /home/duplicity/entrypoint.sh \  
&& touch ${HOME}/dulicity-backup.conf  
  
RUN apk add --no-cache --virtual build-deps \  
linux-headers \  
build-base \  
python-dev \  
libffi-dev \  
openssl-dev \  
py-setuptools \  
py-pip \  
&& pip install --trusted-host pypi.python.org \  
fasteners \  
gsutil \  
s3cmd \  
mega.py \  
python-swiftclient \  
python-keystoneclient \  
&& rm -r ~/.cache/pip \  
&& apk del build-deps \  
&& rm /usr/lib/python2.7/site-packages/mega/mega.pyc \  
&& wget -O /usr/lib/python2.7/site-packages/mega/mega.py
https://raw.githubusercontent.com/tapionx/mega.py/master/mega/mega.py  
VOLUME ["/home/duplicity/.cache/duplicity", "/home/duplicity/.gnupg"]  
  
USER duplicity  
ENV ROOT=/data LOGDIR="/var/log/duplicity/" LOG_FILE="duplicity.log"
LOG_FILE_OWNER="${USER}:${USER}" STATIC_OPTIONS="--allow-source-mismatch"  
  
  
ENTRYPOINT ["bash", "/home/duplicity/entrypoint.sh"]  

