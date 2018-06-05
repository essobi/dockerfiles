  
FROM teego/steemit-bundle-software:latest  
MAINTAINER Aleksandr Zykov <tiger@mano.email>  
  
RUN figlet 'Building'  
  
RUN ( \  
apt-get install -qy --no-install-recommends \  
socat \  
) && \  
apt-get clean -qy  
  
RUN mkdir -p /root/steemit/data/  
  
ADD db-config.json /root/steemit/db/config/config.json  
  
RUN cd /root/steemit/db; \  
cat config/config.json &&\  
( \  
sequelize db:migrate \  
)  
  
ADD config.json /root/steemit/config.json.sample  
  
ADD run-steemit.sh /root/steemit/  
  
RUN ls -l /root/steemit  
  
EXPOSE 3000 3001  
VOLUME ["/root/steemit/data"]  
  
CMD ["/root/steemit/run-steemit.sh"]  
  
RUN figlet 'Happy Steeming'  

