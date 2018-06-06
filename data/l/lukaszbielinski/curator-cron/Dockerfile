FROM janeczku/alpine-kubernetes:3.3  
RUN apk add --update \  
python \  
python-dev \  
py-pip \  
build-base \  
curl \  
jq \  
bash \  
vim \  
&& pip install --upgrade pip \  
&& pip install virtualenv elasticsearch-curator==3.5 \  
&& rm -rf /var/cache/apk/*  
  
COPY curatorcron /var/spool/cron/crontabs/root  
COPY script.sh /script.sh  
COPY configs /configs  
  
CMD crond -l 2 -f  

