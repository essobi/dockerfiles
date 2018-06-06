FROM codeserver/store-base  
MAINTAINER Neil Ellis hello@neilellis.me  
EXPOSE 27017  
EXPOSE 28017  
CMD ["/sbin/my_init"]  
  
ENV USER user  
ENV PASSWORD password  
ENV HOME /root  
WORKDIR /root  
  
RUN apt-get update && \  
apt-get install -y mongodb && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /usr/local/var/mongodb && chown -R store:secure
/usr/local/var/mongodb  
  
RUN for i in `find / -perm +6000 -type f`; do chmod a-s $i; echo "Removed SUID
from $i"; done  
  
# Add run scripts  
RUN mkdir /etc/service/mongodb/  
ADD bin/mongodb.sh /etc/service/mongodb/run  
ADD bin/set_mongodb_password.sh /usr/local/bin/set_mongodb_password.sh  
RUN chmod 775 /etc/service/mongodb/run /usr/local/bin/set_mongodb_password.sh  

