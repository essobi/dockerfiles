FROM zadara/service-cron:alpine  
ENV SSH_SERVER="disabled"  
LABEL description="autoexpand tool for increasing volume capacity dynamically
of a VPSA"  
  
RUN apk --no-cache add jq  
  
ENV VPSA_ACCESS_KEY="" \  
GENERATE_TICKET="enabled" \  
VOLUME_EXPAND_CRITERIA="gb" \  
VOLUME_FREE_GB="100" \  
VOLUME_FREE_PERCENT="5" \  
VOLUME_EXPAND_METHOD="gb" \  
VOLUME_INCREASE_BY_GB="512" \  
VOLUME_INCREASE_BY_PERCENT="5"  
COPY ./scripts /scripts  
COPY ./runonce-storeenv.sh /runonce/000-storeenv.sh  
COPY ./runonce-setCron.sh /runonce/001-setCron.sh  

