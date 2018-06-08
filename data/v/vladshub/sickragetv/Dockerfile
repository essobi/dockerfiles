FROM vladshub/python-virtualenv  
MAINTAINER Vladislav Shub <vlad6il@gmail.com>  
  
RUN apk add --no-cache --update libffi-dev && rm -rf /var/cache/apk/*  
  
EXPOSE 8081  
COPY entrypoint.sh /  
  
ENV SICKRAGE_VERSION 9.1.16  
RUN wget -q
"https://github.com/SiCKRAGETV/SiCKRAGE/archive/$SICKRAGE_VERSION.tar.gz" \  
&& tar xzf *.tar.gz && rm *.tar.gz \  
&& mv SiCKRAGE-* /sickrage  
  
RUN virtualenv /env  
  
WORKDIR /sickrage  
  
RUN . /env/bin/activate \  
&& /env/bin/pip install git+https://github.com/EqUaTe/python-fanart \  
&& /env/bin/pip install --upgrade dogpile.cache \  
&& /env/bin/pip install --upgrade configobj \  
&& /env/bin/pip install --upgrade -r /sickrage/requirements.txt  
  
ENTRYPOINT ["/entrypoint.sh"]  

