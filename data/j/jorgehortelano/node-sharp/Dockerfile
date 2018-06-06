FROM jorgehortelano/node-alpine-edge  
LABEL Description="Sharp library compilation and instalation for docker
Alpine"  
  
ENV VIPS_VERSION 8.5.5  
ENV SHARP_VERSION 0.18.1  
#Compile Vips and Sharp  
RUN apk --no-cache add libpng librsvg libgsf giflib libjpeg-turbo musl \  
&& apk --no-cache add --virtual .build-dependencies g++ make python curl tar
gtk-doc gobject-introspection expat-dev glib-dev libpng-dev libjpeg-turbo-dev
giflib-dev librsvg-dev \  
&& mkdir -p /usr/src \  
&& curl -o vips.tar.gz -SL
https://github.com/jcupitt/libvips/releases/download/v${VIPS_VERSION}/vips-${VIPS_VERSION}.tar.gz
\  
&& tar -xzf vips.tar.gz -C /usr/src/ \  
&& rm vips.tar.gz \  
&& chown -R nobody.nobody /usr/src/vips-${VIPS_VERSION} \  
&& cd /usr/src/vips-${VIPS_VERSION} \  
&& ./configure \  
&& make \  
&& make install \  
&& cd / \  
&& rm -r /usr/src/vips-${VIPS_VERSION} \  
&& su node \  
&& npm install sharp@${SHARP_VERSION} --g --production --unsafe-perm \  
&& chown node:node /usr/local/lib/node_modules -R \  
&& apk del .build-dependencies  

