FROM alpine  
  
LABEL version="1.0"  
LABEL description="Docker container for running Qlik Sense AAI Google
Translate plugin"  
LABEL maintainer="bvk@qlik.com"  
  
RUN apk update \  
&& apk add ca-certificates wget openssl openjdk8  
  
RUN wget https://github.com/wbvreeuwijk/qs-google-
translate/releases/download/v0.1.1-beta/qs-google-translate.zip \  
&& unzip qs-google-translate.zip \  
&& rm qs-google-translate.zip  
  
RUN mkdir /config \  
&& mkdir /translations  
  
ENV GOOGLE_APPLICATION_CREDENTIALS=/config/google.json  
  
VOLUME /config  
VOLUME /translations  
  
EXPOSE 50054  
WORKDIR /config  
CMD ["/qs-google-translate/bin/google-translate-server"]

