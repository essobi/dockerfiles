FROM hence/go:latest  
MAINTAINER Clint Beacock <clint@therefore.ca>  
  
ENV HENCE_APP_NAME=mailhog \  
HENCE_APP_USER=hence \  
HENCE_APP_VERSION=3.2  
  
ENV HENCE_APP_DIR=$HENCE_PREFIX/$HENCE_APP_NAME \  
HENCE_APP_VOL_PREFIX=/hence/$HENCE_APP_NAME  
  
RUN go get github.com/mailhog/MailHog  
  
COPY rootfs /  
  
EXPOSE 1025 8025  
  
VOLUME ["$HENCE_APP_VOL_PREFIX/logs/mailhog-general-logs",
"$HENCE_APP_VOL_PREFIX/logs/mailhog-error-logs"]  

