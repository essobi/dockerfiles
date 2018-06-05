FROM ubuntu:14.04  
MAINTAINER Andres Rojas <andres@conpat.io>  
ENV REFRESHED_AT 2015-04-07  
ENV SEAFILE_VERSION 4.1.2  
ENV SEAFILE_DATA_DIR /seafile/seafile-data  
  
  
# Options  
ENV SEAFILE_SERVER_NAME MySeafile  
ENV SEAFILE_URI localhost  
ENV SEAHUB_ADMIN_EMAIL foo@bar.com  
ENV SEAHUB_ADMIN_PASS baz  
  
  
# Install  
RUN mkdir seafile  
WORKDIR /seafile  
  
RUN apt-get -qq update && apt-get -qqy install \  
python2.7 \  
python-imaging \  
python-setuptools \  
sqlite3 \  
wget  
  
RUN wget https://bitbucket.org/haiwen/seafile/downloads/seafile-
server_${SEAFILE_VERSION}_x86-64.tar.gz  
RUN tar -xzf seafile-server_${SEAFILE_VERSION}_x86-64.tar.gz  
  
RUN mkdir installed  
RUN mv seafile-server_${SEAFILE_VERSION}_x86-64.tar.gz installed  
  
# Configure  
ENV SEAFILE_LD_LIBRARY_PATH /seafile/seafile-
server-${SEAFILE_VERSION}/seafile/lib/:/seafile/seafile-
server-${SEAFILE_VERSION}/seafile/lib64:${LD_LIBRARY_PATH}  
  
RUN mkdir conf  
COPY seafdav.conf conf/  
  
WORKDIR /seafile/seafile-server-${SEAFILE_VERSION}  
RUN LD_LIBRARY_PATH=$SEAFILE_LD_LIBRARY_PATH \  
seafile/bin/ccnet-init \  
\--config-dir=/seafile/ccnet \  
\--name=$SEAFILE_SERVER_NAME \  
\--host=$SEAFILE_URI  
RUN LD_LIBRARY_PATH=$SEAFILE_LD_LIBRARY_PATH \  
seafile/bin/seaf-server-init \  
\--seafile-dir=$SEAFILE_DATA_DIR \  
\--port=12001 \  
\--fileserver-port=8082  
RUN echo $SEAFILE_DATA_DIR > ../ccnet/seafile.ini  
RUN echo "SECRET_KEY = \"$(python seahub/tools/secret_key_generator.py)\"" >
../seahub_settings.py  
  
RUN sqlite3 ../seahub.db ".read seahub/sql/sqlite3.sql" 2>/dev/null 1>&2  
RUN mkdir /seafile/seahub-data  
RUN mv seahub/media/avatars ../seahub-data/avatars  
RUN ln -s ../../../seahub-data/avatars seahub/media  
  
WORKDIR /seafile  
RUN ln -s seafile-server-${SEAFILE_VERSION} seafile-server-latest  
RUN chmod 0600 seahub_settings.py  
RUN chmod 0700 ccnet seafile-data conf  
  
RUN mkdir seafile-data/library-template  
RUN cp -f seafile-server-${SEAFILE_VERSION}/seafile/docs/*.doc seafile-
data/library-template  
  
WORKDIR /seafile/seafile-server-${SEAFILE_VERSION}  
COPY create_admin.py create_admin.py  
RUN ./seafile.sh start && \  
PYTHONPATH=/seafile/seafile-
server-${SEAFILE_VERSION}/seafile/lib64/python2.6/site-packages \  
CCNET_CONF_DIR=/seafile/ccnet \  
python create_admin.py $SEAHUB_ADMIN_EMAIL $SEAHUB_ADMIN_PASS  
RUN rm create_admin.py  
  
# Run  
EXPOSE 10001 12001 8082 8000  
COPY start_services.sh start_services.sh  
  
CMD ["/bin/bash", "start_services.sh"]  

