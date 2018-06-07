FROM gwul/sfm-
base@sha256:bf84472ee4819b86a90a39c184f190b5ab769026eb427fe784625f3148490e55  
MAINTAINER Justin Littman <justinlittman@gwu.edu>  
  
ADD . /opt/sfm-web-harvester/  
WORKDIR /opt/sfm-web-harvester  
RUN pip install -r requirements/common.txt -r requirements/release.txt  
  
CMD sh /opt/sfm-setup/setup_reqs.sh \  
&& appdeps.py --wait-secs 60 --port-wait mq:5672 --port-wait heritrix:8443
--file-wait /sfm-data/collection_set --file-wait /sfm-data/containers \  
&& gosu sfm python web_harvester.py --debug=$DEBUG service mq $RABBITMQ_USER
$RABBITMQ_PASSWORD https://heritrix:8443 $HERITRIX_USER $HERITRIX_PASSWORD
$HERITRIX_CONTACT_URL /sfm-data/containers/$HOSTNAME  

