FROM frolvlad/alpine-glibc  
LABEL maintainer "Alexander Groß <agross@therightstuff.de>"  
  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["upsource", "run"]  
  
EXPOSE 8080  
WORKDIR /upsource  
  
RUN UPSOURCE_VERSION=2018.1.357 && \  
\  
echo Creating upsource user and group with static ID of 6000 && \  
addgroup -g 6000 -S upsource && \  
adduser -g "JetBrains Upsource" -S -h "$(pwd)" -u 6000 -G upsource upsource &&
\  
\  
echo Installing packages && \  
apk add --update coreutils \  
bash \  
wget \  
ca-certificates && \  
\  
DOWNLOAD_URL=https://download.jetbrains.com/upsource/upsource-$UPSOURCE_VERSION.zip
&& \  
echo Downloading $DOWNLOAD_URL to $(pwd) && \  
wget "$DOWNLOAD_URL" \--progress bar:force:noscroll --output-document
upsource.zip && \  
\  
echo Extracting to $(pwd) && \  
unzip ./upsource.zip \  
-d . \  
-x upsource-$UPSOURCE_VERSION/internal/java/linux-amd64/man/* \  
upsource-$UPSOURCE_VERSION/internal/java/windows-amd64/* \  
upsource-$UPSOURCE_VERSION/internal/java/mac-x64/* && \  
rm -f upsource.zip && \  
mv upsource-$UPSOURCE_VERSION/* . && \  
rm -rf upsource-$UPSOURCE_VERSION && \  
\  
chown -R upsource:upsource . && \  
chmod +x /docker-entrypoint.sh  
  
USER upsource  

