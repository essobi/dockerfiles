FROM hypriot/rpi-alpine:3.4  
# install cowsay  
RUN apk update \  
&& apk add git perl \  
&& cd /tmp/ \  
&& git clone https://github.com/jasonm23/cowsay.git \  
&& cd cowsay && ./install.sh /usr/local \  
&& cd .. \  
&& rm -rf cowsay \  
&& apk del git  
  
ENV PATH $PATH  
COPY docker.cow /usr/local/share/cows/  
  
# Move the "default.cow" out of the way so we can overwrite it with
"docker.cow"  
RUN \  
mv /usr/local/share/cows/default.cow /usr/local/share/cows/orig-default.cow \  
&& ln -sv /usr/local/share/cows/docker.cow /usr/local/share/cows/default.cow  
  
ENTRYPOINT ["cowsay"]  

