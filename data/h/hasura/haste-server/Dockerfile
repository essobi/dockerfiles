##  
#  
# Haste docker (Open Source pastebin)  
#  
##  
# use alpine base docker  
FROM alpine  
MAINTAINER ogarcia@connectical.com  
  
# update alpine and install necessary packages  
RUN apk -U --no-progress upgrade && \  
apk -U --no-progress add nodejs  
  
# add software to /srv/haste  
COPY . /srv/haste  
WORKDIR /srv/haste  
  
# build hastebin  
RUN npm install --production  
  
# configure container and run  
EXPOSE 7777  
VOLUME ["/srv/haste/data"]  
ENTRYPOINT ["node"]  
CMD ["server.js"]  

