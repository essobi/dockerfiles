FROM banian/node  
  
# https://github.com/keymetrics/docker-pm2/blob/master/Dockerfile  
RUN yarn global add pm2  
EXPOSE 80 443 43554  
# Start process.yml  
CMD ["pm2-docker", "start", "--auto-exit", "--env", "production",
"process.yml"]  
  
# https://github.com/pm2-hive/pm2-auto-pull  
#RUN pm2 install pm2-auto-pull && \  
# pm2 set pm2-auto-pull:interval 60000  

