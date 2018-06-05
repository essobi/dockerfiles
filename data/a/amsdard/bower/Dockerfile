FROM node  
MAINTAINER Krzysztof Kabala <krzysztof.kabala@amsterdam-standard.pl>  
  
# Install Grunt  
RUN npm install -g bower  
  
# install and cleanup  
RUN apt-get update && apt-get -y install sudo && \  
apt-get -y clean && apt-get -y purge && rm -rf /var/lib/apt/lists/*  
  
# create local user to map in as UID of /opt  
RUN adduser --gecos "First Last,RoomNumber,WorkPhone,HomePhone" \--disabled-
password --home /home/nodejs nodejs && \  
chown nodejs:nodejs -R /home/nodejs  
  
WORKDIR /opt  
  
# run php user as local  
COPY ./entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
# Define default command.  
CMD ["bash"]  

