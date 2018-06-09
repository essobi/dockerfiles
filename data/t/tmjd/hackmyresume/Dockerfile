FROM mhart/alpine-node:latest  
MAINTAINER Erik Stidham <estidham@gmail.com>  
  
# Install bash (for wercker)  
RUN apk update && apk add bash && rm -rf /var/cache/apk/*  
# Install wkthml2pdf  
RUN apk add --no-cache \  
xvfb \  
# Additionnal dependencies for better rendering  
ttf-freefont \  
fontconfig \  
dbus \  
&& \  
# needed for pdf generation  
apk add --no-cache wkhtmltopdf \  
\--repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \  
\--allow-untrusted \  
&& \  
mv /usr/bin/wkhtmltopdf /usr/bin/wkhtmltopdf-origin && \  
echo $'#!/usr/bin/env sh\n\  
Xvfb :0 -screen 0 1024x768x24 -ac +extension GLX +render -noreset & \n\  
DISPLAY=:0.0 wkhtmltopdf-origin --page-size ${PAGE_SIZE:-Letter} $@ \n\  
killall Xvfb\  
' > /usr/bin/wkhtmltopdf && \  
chmod +x /usr/bin/wkhtmltopdf && \  
# Install hackmyresume  
npm install -g hackmyresume && \  
for x in $(\  
# Needed to not run out of heap space for npm search  
node --max-old-space-size=4000 \  
# Search for all themes  
/usr/bin/npm search jsonresume-theme | \  
# Strip colors and cut just the name of the package  
sed -r "s/\x1B\\[([0-9]{1,2}(;[0-9]{1,2})?)?[mGK]//g" | cut -f1 -d' '); \  
do \  
npm install $x; \  
done && \  
for x in $(\  
# Needed to not run out of heap space for npm search  
node --max-old-space-size=4000 \  
# Search for all themes  
/usr/bin/npm search fresh-theme | \  
# Strip colors and cut just the name of the package  
sed -r "s/\x1B\\[([0-9]{1,2}(;[0-9]{1,2})?)?[mGK]//g" | cut -f1 -d' '); \  
do \  
npm install $x; \  
done && \  
rm -rf /root/.npm  

