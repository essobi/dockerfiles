FROM debian:stretch  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
export VNC_ENABLED=true && \  
export EXPOSE_X11=true  
  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install --no-install-recommends --no-install-suggests -y \  
xvfb \  
xauth \  
ca-certificates \  
x11vnc \  
fluxbox \  
xvt \  
curl \  
nano \  
chromedriver  
  
RUN export TINI_VERSION=v0.14.0 && \  
curl -sL
https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini >
/sbin/tini && \  
chmod +x /sbin/tini  
  
RUN sed -i 's/LISTENTCP=""/LISTENTCP="-listen tcp"/' /usr/bin/xvfb-run  
  
RUN mv /usr/lib/chromium/chromium /usr/lib/chromium/chromium-original && \  
printf '%s\n' '#!/bin/sh' 'exec /usr/lib/chromium/chromium-original --no-
sandbox "$@"' \  
> /usr/lib/chromium/chromium && chmod +x /usr/lib/chromium/chromium  
  
RUN ln -s /usr/lib/chromium/chromedriver /usr/local/bin/  
  
RUN apt-get clean  
RUN rm -rf \  
/tmp/* \  
/usr/share/doc/* \  
/var/cache/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
WORKDIR /app  
  
COPY entrypoint.sh /usr/local/bin/entrypoint  
RUN chmod +x /usr/local/bin/entrypoint  
COPY vnc-start.sh /usr/local/bin/vnc-start  
RUN chmod +x /usr/local/bin/vnc-start  
  
# Configure Xvfb via environment variables:  
ENV SCREEN_WIDTH 1440  
ENV SCREEN_HEIGHT 900  
ENV SCREEN_DEPTH 24  
ENV DISPLAY :60  
ENTRYPOINT ["entrypoint"]  
  
# Expose the default webdriver port:  
EXPOSE 4444  
EXPOSE 5900  
CMD ["chromedriver", "--url-base=/wd/hub", "--port=4444", "--whitelisted-
ips="]  

