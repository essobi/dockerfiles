FROM mongo:3.2  
  
# Create fake chown so docker scripts won't fail on Bluemix (ugly hack
ignored)  
#RUN mv /bin/chown /bin/chown.disabled && echo '#!/bin/bash' > /bin/chown &&
echo '/bin/chown.disabled "$@"' >> /bin/chown && echo 'exit 0' >> /bin/chown
&& chmod +x /bin/chown  
  
#RUN apt-get update && apt-get install -y curl lsb-release pwgen  
#RUN curl -O https://repo.stackdriver.com/stack-install.sh && bash stack-
install.sh --write-gcm  
  
# overwrite origin entrypoint  
  
COPY ackee-entrypoint.sh /ackee-entrypoint.sh  
COPY setup_mongo.sh /opt/02-setup-mongo.sh  
#COPY setup_stackdriver.sh /opt/03-setup-stackdriver.sh  
RUN cp /entrypoint.sh /opt/04-mongo-entrypoint.sh && cp /ackee-entrypoint.sh
/entrypoint.sh  

