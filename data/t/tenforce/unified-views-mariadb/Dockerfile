FROM mariadb  
ENV MYSQL_DATABASE=unified_views  
ENV MYSQL_USER=unified_views  
ENV MYSQL_PASSWORD=s00pers3cur3  
ENV MYSQL_ROOT_PASSWORD=s00pers3cur3  
ADD
https://raw.githubusercontent.com/UnifiedViews/Core/UV_Core_v2.3.0/debian/unifiedviews-
backend-mysql/src/deb/usr/share/unifiedviews/mysql/schema.sql /docker-
entrypoint-initdb.d/00-schema.sql  
ADD
https://raw.githubusercontent.com/UnifiedViews/Core/UV_Core_v2.3.0/debian/unifiedviews-
backend-mysql/src/deb/usr/share/unifiedviews/mysql/data-core.sql /docker-
entrypoint-initdb.d/01-data-core.sql  
ADD
https://raw.githubusercontent.com/UnifiedViews/Core/UV_Core_v2.3.0/debian/unifiedviews-
backend-mysql/src/deb/usr/share/unifiedviews/mysql/data-permissions.sql
/docker-entrypoint-initdb.d/02-data-permissions.sql  
ADD
https://raw.githubusercontent.com/UnifiedViews/Core/UV_Core_v2.3.0/debian/unifiedviews-
backend-mysql/src/deb/usr/share/unifiedviews/mysql/2.2.0-update.sql /docker-
entrypoint-initdb.d/03-update.sql  
RUN chmod -R 644 /docker-entrypoint-initdb.d/*  
RUN for x in 00-schema.sql 01-data-core.sql 02-data-permissions.sql
03-update.sql;do sed -i '1s/^/use unified_views;\n/' /docker-entrypoint-
initdb.d/$x;done  
  

