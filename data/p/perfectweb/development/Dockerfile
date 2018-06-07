FROM perfectweb/production:master  
  
# variables setup  
ENV APPLICATION_ENV development  
ENV XDEBUG_INI /etc/php5/mods-available/xdebug.ini  
ENV DBGP_PATH
http://downloads.activestate.com/Komodo/releases/9.1.0/remotedebugging/  
ENV DBGP_VERSION Komodo-PythonRemoteDebugging-9.1.0-87337-linux-x86_64  
  
# php setup  
RUN sed -i.bak 's/display_errors = \\(.*\\)/display_errors = On/g' ${PHP_INI}  
RUN sed -i.bak 's/display_startup_errors = \\(.*\\)/display_startup_errors =
On/g' ${PHP_INI}  
RUN sed -i.bak 's/allow_url_fopen = \\(.*\\)/allow_url_fopen = On/g'
${PHP_INI}  
  
# some php extension changes  
RUN echo -e
'apc.enabled=0\nopcache.enable=0\nxdebug.max_nesting_level=600\nxdebug.remote_enable=true\nxdebug.profiler_enable_trigger=true\nxdebug.remote_host=localhost\nxdebug.remote_port=9000'
>> ${XDEBUG_INI}  
  
# setup dbgproxy  
RUN sed -i.bak "1inohup pydbgpproxy -d 0.0.0.0:9000 -i 0.0.0.0:9001 >>
${LOGS_DIR}/php.log&" ${HOME_DIR}/run.sh  
RUN wget -O /usr/local/pydbgp.tar.gz ${DBGP_PATH}${DBGP_VERSION}.tar.gz; tar
xvf /usr/local/pydbgp.tar.gz -C /usr/local/; rm -rf /usr/local/pydbgp.tar.gz ;
ln -s /usr/local/${DBGP_VERSION}/pydbgpproxy /usr/bin/pydbgpproxy ; wget
https://bootstrap.pypa.io/get-pip.py; python get-pip.py; pip install dbgp; rm
-f get-pip.py  
  
# tips  
## if you want to use your local mysql server or anything else that runs on
socket you can add `-v /var/lib/mysql/mysql.sock:/var/run/mysqld/mysqld.sock`
to your run command (replace the path with the sock path you wanna mount)  
# paths  
# sphinx: /etc/sphinxsearch/sphinx.conf  
# mysql: /var/run/mysqld/mysqld.sock  

