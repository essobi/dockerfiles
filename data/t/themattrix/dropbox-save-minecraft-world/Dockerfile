FROM alpine:latest  
  
# proper init  
ADD https://github.com/krallin/tini/releases/download/v0.14.0/tini-static
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
RUN apk --update add curl bash && \  
rm -rf /var/cache/apk/*  
  
ADD https://raw.githubusercontent.com/andreafabrizi/Dropbox-
Uploader/a00ccc35dd2e54f70575e10995eb9b76a1ef7aea/dropbox_uploader.sh \  
/usr/bin/dropbox_uploader.sh  
RUN chmod +x /usr/bin/dropbox_uploader.sh  
  
COPY save-to-dropbox.sh /usr/bin/save-to-dropbox.sh  
RUN chmod +x /usr/bin/save-to-dropbox.sh  
  
# world data and settings expected to be mounted here  
WORKDIR /volumes  
  
CMD ["save-to-dropbox.sh"]  

