# 3DCityDB WFS Dockerfile
#####################################################  
# Official website https://www.3dcitydb.net  
# GitHub https://github.com/3dcitydb/web-feature-service  
###############################################################################  
# Base image  
ARG baseimage_tag="8.5-jre8"  
FROM tomcat:${baseimage_tag}  
# Maintainer
##################################################################  
# Bruno Willenborg  
# Chair of Geoinformatics  
# Department of Civil, Geo and Environmental Engineering  
# Technical University of Munich (TUM)  
# <b.willenborg@tum.de>  
MAINTAINER Bruno Willenborg, Chair of Geoinformatics, Technical University of
Munich (TUM) <b.willenborg@tum.de>  
  
# Setup 3DCityDB WFS
##########################################################  
ARG citydb_wfs_version=3.3.1  
ENV CITYDB_WFS_VERSION=${citydb_wfs_version}  
  
ARG citydb_wfs_context_path="citydb-wfs"  
ENV CITYDB_WFS_CONTEXT_PATH=${citydb_wfs_context_path}  
  
RUN set -x \  
&& cd $HOME \  
&& echo 'deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main' >
/etc/apt/sources.list.d/pgdg.list \  
&& wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-
key add - \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates postgresql-client-10 xmlstarlet && rm -rf /var/lib/apt/lists/* \  
&& wget "https://github.com/3dcitydb/web-feature-
service/releases/download/v${CITYDB_WFS_VERSION}/citydb-
wfs-${CITYDB_WFS_VERSION}.zip" -O 3dcitydb-wfs.zip \  
&& mkdir -p 3dcitydb-wfs && unzip -j -d 3dcitydb-wfs 3dcitydb-wfs.zip
"*/citydb-wfs.war" "*/lib/*.jar" && rm 3dcitydb-wfs.zip \  
&& cp 3dcitydb-wfs/*.jar /usr/local/tomcat/lib/ \  
&& unzip 3dcitydb-wfs/citydb-wfs.war -d
/usr/local/tomcat/webapps/${CITYDB_WFS_CONTEXT_PATH} \  
&& rm -r 3dcitydb-wfs \  
&& apt-get purge -y --auto-remove wget  
  
# Setup 3DCityDB WFS container entrypoint
#####################################  
COPY citydb-wfs.sh /usr/local/bin/  
RUN ln -s usr/local/bin/citydb-wfs.sh / # backwards compat  
RUN chmod u+x /usr/local/bin/citydb-wfs.sh  
  
# wait-for-psql script  
COPY wait-for-psql.sh /usr/local/bin/  
RUN ln -s usr/local/bin/wait-for-psql.sh / # backwards compat  
RUN chmod u+x /usr/local/bin/wait-for-psql.sh  
  
ENTRYPOINT ["citydb-wfs.sh"]  
CMD ["catalina.sh","run"]  
  

