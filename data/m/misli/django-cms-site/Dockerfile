FROM ubuntu  
  
LABEL name="django CMS"  
LABEL maintainer="Jakub Dorňák <jakub.dornak@misli.cz>"  
  
ENV PYTHONPATH=/app  
ENV PYTHONUNBUFFERED 1  
WORKDIR /app  
  
# install requirements and generate czech locale  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install locales supervisor nginx memcached sqlite3
libmysqlclient-dev mariadb-client postgresql-client python-dev python-pip \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& pip install --upgrade pip \  
&& echo cs_CZ.UTF-8 UTF-8 > /etc/locale.gen && locale-gen  
ENV LC_ALL cs_CZ.UTF-8  
# install required packages  
COPY requirements.txt /app/  
RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt  
  
# install cms_site  
COPY . /src  
RUN pip install --no-cache-dir /src \  
&& cp -a /src/translations/* /usr/local/lib/python2.7/dist-packages/ \  
&& cp -a /src/conf /src/bin ./ \  
&& rm -r /src \  
&& mkdir -p data htdocs/media htdocs/static run \  
&& django-cms collectstatic --no-input \  
&& chown www-data:www-data data htdocs/media run  
  
# fix bug in cmsplugin-filer  
RUN sed -i 's/BaseImage.objects.none/File.objects.none/' \  
/usr/local/lib/python2.7/dist-packages/cmsplugin_filer_folder/cms_plugins.py
|| :  
  
CMD ["/app/bin/run-supervisord"]  

