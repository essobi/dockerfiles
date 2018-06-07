FROM alpine:latest  
MAINTAINER My Social Observations <mysocialobservations@gmail.com>  
  
ENV HUGO_VERSION='0.15' \  
HUGO_FILE_EXTENSION='tar.gz' \  
HUGO_FOLDER_POSTFIX='linux_amd64'  
RUN apk add --update --update-cache --no-cache \  
wget \  
ca-certificates && \  
wget
"https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_${HUGO_FOLDER_POSTFIX}.${HUGO_FILE_EXTENSION}"
&& \  
tar xzf "hugo_${HUGO_VERSION}_${HUGO_FOLDER_POSTFIX}.${HUGO_FILE_EXTENSION}"
&& \  
rm -r "hugo_${HUGO_VERSION}_${HUGO_FOLDER_POSTFIX}.${HUGO_FILE_EXTENSION}" &&
\  
mv
"hugo_${HUGO_VERSION}_${HUGO_FOLDER_POSTFIX}/hugo_${HUGO_VERSION}_${HUGO_FOLDER_POSTFIX}"
/usr/bin/hugo && \  
rm -r "hugo_${HUGO_VERSION}_${HUGO_FOLDER_POSTFIX}" && \  
apk del --update --update-cache --no-cache \  
wget \  
ca-certificates  
  
COPY ./run.sh /run.sh  

