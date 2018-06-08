# Builder (stage 0)  
FROM dpwrussell/omero-web-extended  
  
ARG PYTHONPATH=/opt/omero/web/venv/lib/python2.7/site-
packages/:/opt/omero/web/OMERO.web/lib/python/  
  
RUN /opt/omero/web/OMERO.web/bin/omero web config nginx >
/opt/omero/web/nginx_omero-web.conf \  
&& sed -i -re 's/(alias
)\/opt\/omero\/web\/OMERO.web\/lib\/python\/omeroweb\/static(;)/\1\/opt\/omero\/nginx\/static\2/'
/opt/omero/web/nginx_omero-web.conf \  
&& python /opt/omero/web/OMERO.web/lib/python/omeroweb/manage.py collectstatic
\--noinput  
# Production  
FROM nginx  
MAINTAINER douglas_russell@hms.harvard.edu  
  
COPY --from=0 /opt/omero/web/OMERO.web/lib/python/omeroweb/static
/opt/omero/nginx/static/  
COPY --from=0 /opt/omero/web/nginx_omero-web.conf /etc/nginx/conf.d/omero-
web.conf  
  
RUN sed -i.bak -re 's/( default_server.*)/; #\1/' /etc/nginx/nginx.conf \  
&& mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.disabled  
  
ADD ms-thumbnails_upstream.conf ms-thumbnails_locations.conf ms-image-
region_upstream.conf ms-image-region_locations.conf /etc/nginx/  
ADD entrypoint.sh /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

