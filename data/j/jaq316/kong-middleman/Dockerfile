FROM kong:0.11-alpine  
LABEL maintainer Jacques Snyman, jacques@jacquessnyman.co.za  
  
ENV MIDDLEMAN_VERSION 0.1.1-1  
  
RUN apk add --no-cache git zip \  
&& git clone https://github.com/pantsel/kong-middleman-plugin middleman-src \  
&& cd middleman-src \  
&& luarocks make \  
&& luarocks pack middleman $MIDDLEMAN_VERSION \  
&& luarocks install middleman-$MIDDLEMAN_VERSION.all.rock \  
&& cd \- \  
&& rm -r middleman-src \  
&& apk del git zip  
  
ENV KONG_CUSTOM_PLUGINS middleman  
  

