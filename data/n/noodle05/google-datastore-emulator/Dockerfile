FROM google/cloud-sdk:193.0.0-alpine  
  
ENV LISTEN_PORT="8282" \  
LISTEN_HOST="0.0.0.0" \  
PROJECT_NAME="pname" \  
DATA_DIR="/var/lib/datastore"  
RUN apk --no-cache --update add openjdk8-jre \  
&& gcloud components install cloud-datastore-emulator beta \  
&& mkdir -p "${DATA_DIR}" \  
&& rm -fr /var/cache/apk/*  
  
VOLUME "${DATA_DIR}"  
  
EXPOSE 8282  
ADD datastore-emulator.sh /  
  
CMD [ "/datastore-emulator.sh" ]  

