FROM ubuntu:latest  
  
ENV SANDBOX_USERCSS="Normal:+/etc/shellinabox/options-enabled/00+Green-On-
Black.css;Colors:+/etc/shellinabox/options-enabled/01+Color-Terminal.css" \  
SANDBOX_PORT=4200 \  
SANDBOX_ADDUSER=true \  
SANDBOX_USER=guest \  
SANDBOX_GROUP=guest \  
SANDBOX_PASSWORD=password \  
SANDBOX_SUDO=true \  
SANDBOX_SSL=false \  
SANDBOX_SERVICE=/:LOGIN  
  
ADD scripts/* /usr/local/sbin/  
ADD css/* /etc/shellinabox/options-enabled/  
  
RUN apt-get update && apt-get install -y sudo openssl curl openssh-client
shellinabox && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
ln -sf '/etc/shellinabox/options-enabled/00+Green On Black.css' \  
/etc/shellinabox/options-enabled/00+Green-On-Black.css && \  
ln -sf '/etc/shellinabox/options-enabled/01+Color Terminal.css' \  
/etc/shellinabox/options-enabled/01+Color-Terminal.css  
  
EXPOSE 4200  
ENTRYPOINT ["entrypoint.sh"]  
  
CMD ["run"]  

