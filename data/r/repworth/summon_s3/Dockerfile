FROM frolvlad/alpine-glibc  
  
ENV SUMMON_PROVIDER_INSTALL_DIR=/usr/libexec/summon  
ENV SUMMON_PROVIDER_ZIP_FILE_NAME=summon-s3_v0.1.0_linux_amd64.zip  
ENV SUMMON_TAR_FILE_NAME=summon_v0.3.0_linux_amd64.tar.gz  
  
# install dependent packages  
RUN apk -U add ca-certificates wget  
  
# install summon & cleanup  
RUN \  
wget
https://github.com/conjurinc/summon/releases/download/v0.3.0/$SUMMON_TAR_FILE_NAME
&& \  
tar -C /usr/local/bin -zxf $SUMMON_TAR_FILE_NAME && \  
rm $SUMMON_TAR_FILE_NAME  
  
# install summon s3 provider & cleanup  
RUN \  
wget
https://github.com/conjurinc/summon-s3/releases/download/v0.1.0/$SUMMON_PROVIDER_ZIP_FILE_NAME
&& \  
mkdir -p $SUMMON_PROVIDER_INSTALL_DIR && \  
unzip $SUMMON_PROVIDER_ZIP_FILE_NAME -d $SUMMON_PROVIDER_INSTALL_DIR && \  
rm $SUMMON_PROVIDER_ZIP_FILE_NAME  
  
# cleanup apk  
RUN rm /var/cache/apk/*

