FROM digitallyseamless/nodejs-bower-grunt  
  
# install and cleanup  
RUN apt-get update && apt-get -y install sudo && \  
apt-get -y clean && apt-get -y purge && rm -rf /var/lib/apt/lists/*  
  
# create local user to map in as UID of /opt  
RUN adduser --disabled-password --home /home/nodejs nodejs  
  
# storing composer cache locally instead of docker  
VOLUME /home/nodejs  
  
WORKDIR /opt  
  
# run php user as local  
COPY ./entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

