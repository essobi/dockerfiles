FROM node:5.10.0  
RUN npm install -g bower@1.7.9 && \  
useradd -d /home/tester tester && \  
mkdir -p /home/tester/app && \  
chown -R tester /home/tester && \  
mkdir /input && \  
chown -R tester /input  
  
VOLUME /input  
COPY ./docker-entrypoint.sh /home/tester  
RUN chmod +x /home/tester/docker-entrypoint.sh  
USER tester  
ENTRYPOINT ["/home/tester/docker-entrypoint.sh"]  
CMD ["help"]  

