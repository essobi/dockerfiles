FROM openjdk:7-jre-alpine  
  
RUN apk --no-cache add curl unzip sudo  
  
RUN curl -o crowdin-cli.zip -SL https://downloads.crowdin.com/cli/v2/crowdin-
cli.zip \  
&& unzip -j crowdin-cli.zip \  
&& sh crowdin.sh \  
&& rm *.*  
  
ADD entrypoint.sh /usr/local/bin/crowdin  
  
ENTRYPOINT [ "crowdin" ]  

