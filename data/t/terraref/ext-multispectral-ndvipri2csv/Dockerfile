FROM terraref/terrautils  
MAINTAINER Max Burnette <mburnet2@illinois.edu>  
  
# TODO: Dockerhub automated builds from tags  
# Create user with necessary user ID for writing permissions on Roger  
RUN useradd -u 49044 extractor \  
&& mkdir -p /home/extractor/sites/ua-mac/raw_data \  
&& mkdir -p /home/extractor/sites/ua-mac/Level_1/bin2csv \  
&& chown -R extractor /home/extractor  
  
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
RABBITMQ_QUEUE="terra.multispectral.ndvipri2csv" \  
MOUNTED_PATHS='{"home/clowder/sites":"/home/extractor/sites"}' \  
MAIN_SCRIPT="terra_ndvipri2csv.py"  

