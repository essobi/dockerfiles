FROM gcr.io/earthengine-project/datalab-ee:latest  
# Use testing to get GDAL2  
COPY testing.list /etc/apt/sources.list.d/testing.list  
RUN apt-get update && yes | apt-get install apt-utils  
RUN apt-get update && yes | apt-get install gdal-bin python-imaging-tk python-
imaging python-gdal build-essential apache2 apache2-utils  
RUN git clone https://github.com/samapriya/Planet-GEE-Pipeline-CLI.git && cd
Planet-GEE-Pipeline-CLI && python setup.py install && pip install -r
requirements.txt  
RUN git clone https://github.com/tracek/gee_asset_manager.git && cd
gee_asset_manager && pip install -e .  
COPY vhost.conf /etc/apache2/sites-enabled/000-default.conf  
RUN a2enmod proxy_http proxy_wstunnel rewrite  
ENTRYPOINT htpasswd -cb /etc/apache2/.htpasswd datalab ${PASSWORD:-datalab} &&
service apache2 restart && /datalab/run.sh  

