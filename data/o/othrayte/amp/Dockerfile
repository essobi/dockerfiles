#  
# AMP Dockerfile  
#  
# https://github.com/othrayte/docker-cc-amp  
#  
# Pull base image.  
FROM cubecoders/ampbase  
  
RUN \  
groupadd -r AMP && \  
useradd -r -g AMP -d /home/AMP -m AMP && \  
mkdir /home/AMP/AMP  
  
# Define working directory.  
WORKDIR /home/AMP/AMP  
  
COPY start.sh /home/AMP/AMP/  
  
RUN \  
mkdir /ampdata && \  
chown AMP:AMP /ampdata && \  
chown AMP:AMP /home/AMP/AMP && \  
chown AMP:AMP ./start.sh && \  
chmod +x ./start.sh  
  
VOLUME ["/ampdata"]  
  
USER AMP  
  
# Define default command.  
ENTRYPOINT ["./start.sh"]  
  
RUN ln -s /ampdata /home/AMP/.ampdata  
  
# Expose ports.  
EXPOSE 8080  

