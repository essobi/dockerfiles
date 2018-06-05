FROM terraref/terrautils  
MAINTAINER Max Burnette <mburnet2@illinois.edu>  
  
# Install any programs needed  
# TODO: Can we remove this user ID and mount files as Max?  
RUN useradd -u 49044 extractor \  
&& apt-get install -y -q gfortran \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /home/extractor/sites/ua-mac/raw_data \  
&& mkdir -p /home/extractor/sites/ua-mac/Level_1/stereoTop_geotiff \  
&& chown -R extractor /home/extractor  
  
RUN pip install terraref-stereo-rgb  
  
# command to run when starting docker  
COPY entrypoint.sh extractor_info.json *.py /home/extractor/  
  
USER extractor  
ENTRYPOINT ["/home/extractor/entrypoint.sh"]  
CMD ["extractor"]  
  
# Setup environment variables. These are passed into the container. You can
change  
# these to your setup. If RABBITMQ_URI is not set, it will try and use the
rabbitmq  
# server that is linked into the container. MAIN_SCRIPT is set to the script
to be  
# executed by entrypoint.sh  
ENV RABBITMQ_EXCHANGE="terra" \  
RABBITMQ_VHOST="%2F" \  
RABBITMQ_QUEUE="terra.stereo-rgb.bin2tif" \  
MAIN_SCRIPT="terra_bin2tif.py"  

