FROM carllhw/odoo-dev:8.0  
  
LABEL maintainer="Haiwei Liu <carllhw@gmail.com>"  
  
USER root  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
freetds-dev \  
libffi-dev \  
&& apt-get -y install -f --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
# cx_Oracle  
ENV ORACLE_HOME /opt/oracle/instantclient_12_1  
ENV LD_RUN_PATH=$ORACLE_HOME  
RUN set -x \  
&& curl -o /tmp/instantclient-basic-linux.x64-12.1.0.2.0.zip -SL
http://files.saas.hand-china.com/oracle/instantclient/instantclient-basic-
linux.x64-12.1.0.2.0.zip \  
&& curl -o /tmp/instantclient-sdk-linux.x64-12.1.0.2.0.zip -SL
http://files.saas.hand-china.com/oracle/instantclient/instantclient-sdk-
linux.x64-12.1.0.2.0.zip \  
&& mkdir -p /opt/oracle \  
&& unzip "/tmp/instantclient*.zip" -d /opt/oracle \  
&& ln -s $ORACLE_HOME/libclntsh.so.12.1 $ORACLE_HOME/libclntsh.so \  
&& rm -rf /tmp/instantclient*.zip  
  
COPY ./requirements.txt /usr/src/hrp/  
RUN pip install --no-cache-dir -r /usr/src/hrp/requirements.txt  
  
USER odoo  

