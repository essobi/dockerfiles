FROM alpine  
MAINTAINER Ciel <me@ciel.im>  
  
RUN apk --update add \  
bash curl  
RUN curl -s "https://raw.githubusercontent.com/andreafabrizi/Dropbox-
Uploader/master/dropbox_uploader.sh" \  
-o /usr/bin/dropbox_uploader.sh && chmod +x /usr/bin/dropbox_uploader.sh  
  
ENTRYPOINT ["dropbox_uploader.sh"]  

