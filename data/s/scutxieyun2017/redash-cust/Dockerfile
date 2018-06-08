FROM redash/redash:v2.0.0  
USER root  
RUN apt-get update -y  
RUN apt-get install libaio-dev -y  
USER redash  
COPY package.json /app/package.json  
RUN npm install  
COPY webpack.config.js /app/webpack.config.js  
COPY client/.eslintrc.js /app/client/.eslintrc.js  
COPY client/app/services/index.js /app/client/app/services/index.js  
COPY client/app/utils/index.js /app/client/app/utils/index.js  
COPY client/app/utils/data2xlsx.js /app/client/app/utils/data2xlsx.js  
COPY client/app/pages/queries/visualization-embed.html
/app/client/app/pages/queries/visualization-embed.html  
COPY client/app/pages/queries/visualization-embed.js
/app/client/app/pages/queries/visualization-embed.js  
COPY client/app/pages/dashboards/widget.html
/app/client/app/pages/dashboards/widget.html  
COPY client/app/pages/dashboards/widget.js
/app/client/app/pages/dashboards/widget.js  
COPY client/app/pages/queries/view.js /app/client/app/pages/queries/view.js  
COPY client/app/services/query.js /app/client/app/services/query.js  
COPY client/app/services/auth.js /app/client/app/services/auth.js  
COPY client/app/services/query-result.js /app/client/app/services/query-
result.js  
COPY client/app/components/parameters.js
/app/client/app/components/parameters.js  
COPY client/app/components/parameters.html
/app/client/app/components/parameters.html  
COPY client/app/pages/queries/query.html
/app/client/app/pages/queries/query.html  
COPY client/app/pages/dashboards/dashboard.html
/app/client/app/pages/dashboards/dashboard.html  
COPY client/app/pages/queries-list/index.js /app/client/app/pages/queries-
list/index.js  
COPY client/app/components/app-header/app-header.html
/app/client/app/components/app-header/app-header.html  
COPY client/app/visualizations/pivot/index.js
/app/client/app/visualizations/pivot/index.js  
RUN npm run build  
COPY contribute/oracle/oracle-instantclient12.2-basic_12.2.0.1.0-2_amd64.deb
/tmp  
USER root  
RUN dpkg -i /tmp/oracle-instantclient12.2-basic_12.2.0.1.0-2_amd64.deb  
RUN ln -s /usr/lib/oracle/12.2/client64/lib/libclntsh.so.12.1
/usr/lib/oracle/12.2/client64/lib/libclntsh.so  
RUN echo "/usr/lib/oracle/12.2/client64/lib/" > /etc/ld.so.conf.d/oracle.conf  
RUN /sbin/ldconfig  
RUN pip install cx_oracle  
USER redash  
  
COPY redash/query_runner/oracle.py /app/redash/query_runner/oracle.py  
COPY redash/settings.py /app/redash/settings.py  
COPY redash/models.py /app/redash/models.py  
COPY redash/authentication/__init__.py /app/redash/authentication/__init__.py  
COPY redash/authentication/cas_auth.py /app/redash/authentication/cas_auth.py  
COPY redash/authentication/pycas.py /app/redash/authentication/pycas.py  
COPY redash/authentication/google_oauth.py
/app/redash/authentication/google_oauth.py  
COPY redash/handlers/authentication.py /app/redash/handlers/authentication.py  
COPY redash/handlers/query_results.py /app/redash/handlers/query_results.py  
  
ENTRYPOINT ["/bin/bash"]

