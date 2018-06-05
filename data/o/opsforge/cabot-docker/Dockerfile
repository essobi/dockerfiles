FROM python:2.7  
MAINTAINER opsforge.io  
LABEL name="cabot"  
LABEL version="0.0.2"  
  
ENV PYTHONUNBUFFERED 1  
EXPOSE 5001  
RUN mkdir /code  
  
WORKDIR /code  
  
RUN apt-get update && apt-get install -y \  
python-dev \  
libsasl2-dev \  
libldap2-dev \  
libpq-dev \  
npm && \  
apt-get clean  
  
RUN npm install -g \  
\--registry http://registry.npmjs.org/ \  
coffee-script \  
less@1.3  
  
RUN ln -s `which nodejs` /usr/bin/node  
  
RUN pip install --upgrade pip  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY requirements-plugins.txt ./  
RUN pip install --no-cache-dir -r requirements-plugins.txt  
  
RUN pip install ipdb  
  
ADD . /code/  
  
COPY docker-entrypoint.sh /root/  
  
RUN chmod 0755 /root/docker-entrypoint.sh  
  
ENTRYPOINT ["/root/docker-entrypoint.sh"]  

