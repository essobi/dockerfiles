FROM debian:testing  
COPY ./start.sh start.sh  
ENV instancename docker_book  
ENV booktypeversion 2.0  
#env DJANGO_SETTINGS_MODULE ${instancename}.settings  
ENV HTTP_HOST localhost  
ENV DJANGO_SETTINGS_MODULE settings.prod  
ENV PYTHONPATH
$PYTHONPATH://:/${instancename}/lib/:/Booktype/lib:/${instancename}  
ENV BOOKTYPE_USER booktype  
ENV BOOKTYPE_PASS booktype  
ENV BOOKTYPE_DB booktype  
ENV PG_HOST booktyppostgres  
ENV PG_PORT '5432'  
ENV REDIS_HOST 'booktyperedis'  
EXPOSE 8000  
EXPOSE 8080  
#VOLUME /  
VOLUME /logs  
  
RUN apt-get update && apt-get -y upgrade  
  
# Install needed packages as root  
RUN apt-get install -y wget \  
unzip \  
python \  
python-dev \  
git-core \  
python-pip \  
python-virtualenv \  
redis-server \  
libxml2-dev \  
libxslt-dev \  
zlib1g-dev \  
libpq-dev  
  
# Create Python Virtual Environment  
RUN virtualenv --distribute /docker_booktype  
RUN #!/bin/bash . /docker_booktype/bin/activate  
  
# Fetch Booktype source  
RUN wget
https://github.com/sourcefabric/Booktype/archive/${booktypeversion}.zip  
RUN unzip /${booktypeversion}.zip  
RUN ln -s /Booktype-${booktypeversion} /Booktype  
RUN rm /${booktypeversion}.zip  
  
# Install needed Python modules  
RUN pip install -r /Booktype/requirements/prod.txt  
  
# Create Booktype project  
RUN /Booktype/scripts/createbooktype --database postgresql ${instancename}  
  
#RUN cp -R /${instancename}/docker_book_site/settings
/${instancename}/settings  
RUN mkdir -p /${instancename}/settings  
RUN ls -lah /${instancename}/settings  
#RUN rm -f /${instancename}/settings/prod.py  
COPY ./prod.py /${instancename}/settings/prod.py  
COPY ./base.py /${instancename}/settings/base.py  
#RUN cat /${instancename}/settings/prod.py  
CMD ["/bin/bash", "start.sh"]  

