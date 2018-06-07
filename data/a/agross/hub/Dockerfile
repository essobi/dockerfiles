FROM frolvlad/alpine-glibc  
LABEL maintainer "Alexander Groß <agross@therightstuff.de>"  
  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["hub", "run"]  
  
EXPOSE 8080  
WORKDIR /hub  
  
RUN HUB_VERSION=2018.2.9541 && \  
\  
echo Creating hub user and group with static ID of 4000 && \  
addgroup -g 4000 -S hub && \  
adduser -g "JetBrains Hub" -S -h "$(pwd)" -u 4000 -G hub hub && \  
\  
echo Installing packages && \  
apk add --update coreutils \  
bash \  
wget \  
ca-certificates && \  
\  
DOWNLOAD_URL=https://download.jetbrains.com/hub/hub-$HUB_VERSION.zip && \  
echo Downloading $DOWNLOAD_URL to $(pwd) && \  
wget "$DOWNLOAD_URL" \--progress bar:force:noscroll --output-document hub.zip
&& \  
\  
echo Extracting to $(pwd) && \  
unzip ./hub.zip \  
-d . \  
-x hub-$HUB_VERSION/internal/java/linux-amd64/man/* \  
hub-$HUB_VERSION/internal/java/windows-amd64/* \  
hub-$HUB_VERSION/internal/java/mac-x64/* && \  
rm -f hub.zip && \  
mv hub-$HUB_VERSION/* . && \  
rm -rf hub-$HUB_VERSION && \  
\  
chown -R hub:hub . && \  
chmod +x /docker-entrypoint.sh  
  
USER hub  

