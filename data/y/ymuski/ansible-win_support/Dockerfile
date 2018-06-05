FROM alpine:3.5  
MAINTAINER Yury Muski <muski.yury@gmail.com>  
  
RUN \  
apk --update add sudo && \  
apk --update add gcc python py-pip openssl-dev python-dev libffi-dev musl-dev
&& \  
rm -rf /var/cache/apk/*  
RUN \  
pip install --no-cache-dir --upgrade pip cffi && \  
pip install --no-cache-dir
http://github.com/diyan/pywinrm/archive/master.zip#egg=pywinrm && \  
pip install --no-cache-dir "pywinrm>=0.2.2" && \  
pip install --no-cache-dir pywinrm[credssp] --upgrade && \  
pip install --no-cache-dir ansible  
  
RUN mkdir /ansible  
  
WORKDIR /ansible  
  
ENTRYPOINT ["ansible-playbook"]

