FROM python:3.6  
ENV DEBIAN_FRONTEND=noninteractive  
ARG USER=superset  
  
COPY superset /home/$USER  
  
SHELL ["bash", "-c"]  
  
ARG WORK=/opt/oracle  
ENV ORACLE_HOME=$WORK/instantclient_12_2  
ARG ORACLE_INSTANT_CLIENT=12.2.0.1.0  
ENV PATH=$PATH:$ORACLE_HOME \  
LD_LIBRARY_PATH=$ORACLE_HOME  
  
ENV LANG=C.UTF-8 \  
LC_ALL=C.UTF-8 \  
PATH=$PATH:/home/$USER/.bin \  
PYTHONPATH=/home/$USER/.superset:$PYTHONPATH \  
SQLALCHEMY_DATABASE_URI=sqlite:////home/$USER/.superset/$USER.db  
  
RUN apt-get -qqy update && mkdir -p $WORK && \  
apt-get -qqy install unzip libaio-dev \  
build-essential \  
libsasl2-dev \  
libldap2-dev \  
mariadb-client \  
postgresql-client && \  
wget -qSL https://github.com/bumpx/oracle-
instantclient/raw/master/instantclient-basic-
linux.x64-$ORACLE_INSTANT_CLIENT.zip -O /tmp/instantclient-basic.zip && unzip
/tmp/instantclient-basic.zip -d $WORK && \  
wget -qSL https://github.com/bumpx/oracle-
instantclient/raw/master/instantclient-sqlplus-
linux.x64-$ORACLE_INSTANT_CLIENT.zip -O /tmp/instantclient-sqlplus.zip &&
unzip /tmp/instantclient-sqlplus.zip -d $WORK && \  
wget -qSL https://github.com/bumpx/oracle-
instantclient/raw/master/instantclient-sdk-
linux.x64-$ORACLE_INSTANT_CLIENT.zip -O /tmp/instantclient-sdk.zip && unzip
/tmp/instantclient-sdk.zip -d $WORK && \  
ln -s $ORACLE_HOME/libclntsh.so.12.1 $ORACLE_HOME/libclntsh.so && \  
ln -s $ORACLE_HOME/libocci.so.12.1 $ORACLE_HOME/libocci.so && \  
echo "$ORACLE_HOME" | tee -a /etc/ld.so.conf.d/oracle_instant_client.conf &&
ldconfig && \  
pip install cython numpy pandas && \  
pip install cx_Oracle && \  
pip install superset redis \  
pyldap flask-mail flask-oauth flask_oauthlib \  
mysqlclient psycopg2 pyhive \  
impyla \  
PyAthenaJDBC \  
sqlalchemy-redshift \  
sqlalchemy-clickhouse \  
sqlalchemy-vertica-python && \  
useradd -b /home -U -m $USER && \  
touch /home/$USER/.superset/$USER.db && \  
chmod +x /home/$USER/.bin/* && \  
chown -R $USER:$USER /home/$USER && \  
\  
INSTALL_PATH=/sbin \  
TINI_VERSION=0.14.0 \  
TINI_SHA=b2d2b6d7f570158ae5eccbad9b98b5e9f040f853 \  
GOSU_SHA=8068f973713558e750b5cbe74e2c5a40d6aeb631 \  
GOSU_VERSION=1.10 && \  
curl -fsSL
https://github.com/krallin/tini/releases/download/v$TINI_VERSION/tini-static-
amd64 \  
-o $INSTALL_PATH/tini ; echo "$TINI_SHA $INSTALL_PATH/tini" | sha1sum -c - && \  
curl -fsSL
https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64 \  
-o $INSTALL_PATH/gosu ; echo "$GOSU_SHA $INSTALL_PATH/gosu" | sha1sum -c - && \  
chmod +x $INSTALL_PATH/* && \  
rm -rf /var/cache/apt/* /var/lib/apt/lists/* /var/log/* /tmp/* ~/.[^.]*  
  
WORKDIR /home/$USER  
VOLUME /home/$USER/.superset  
  
EXPOSE 8088  
HEALTHCHECK CMD ["curl", "-f", "localhost:8088/health"]  
ENTRYPOINT ["tini", "-s", "--"]  
CMD ["superset", "runserver"]  
USER $USER  

