FROM ckan/ckan  
  
RUN ckan-pip install git+https://github.com/chrodriguez/ckanext-
senasa_theme.git && \  
ckan-pip install ckanext-envvars  
USER root  
RUN sed -i '/ckan-paster make-config/a sed -ri "s/(ckan.plugins.*$)/\\\1
senasa_theme envvars/" $CONFIG' /ckan-entrypoint.sh  
USER ckan  

