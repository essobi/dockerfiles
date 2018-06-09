  
FROM debian:buster-slim  
LABEL maintainer="06kellyjac@googlemail.com"  
ENV VERSION 0.0.5  
ENV XDG_CONFIG_HOME=/  
RUN apt-get update &&\  
apt-get install -y --no-install-recommends \  
ca-certificates \  
curl &&\  
apt-get install -y --no-install-recommends \  
gconf2 \  
gconf-service \  
libappindicator1 \  
libasound2 \  
libatk1.0-0 \  
libcairo2 \  
libcups2 \  
libexpat1 \  
libfontconfig1 \  
libfreetype6 \  
libgtk2.0-0 \  
libnotify4 \  
libnss3 \  
libpango-1.0-0 \  
libx11-xcb1 \  
libxcomposite1 \  
libxcursor1 \  
libxdamage1 \  
libxext6 \  
libxfixes3 \  
libxi6 \  
libxrandr2 \  
libxrender1 \  
libxss1 \  
libxtst6 &&\  
curl -sSL https://github.com/ivelkov/teams-for-
linux/releases/download/v${VERSION}/teams-for-linux_${VERSION}_amd64.deb -o
/tmp/teams.deb &&\  
dpkg -i /tmp/teams.deb &&\  
apt-get remove --purge -y curl ca-certificates && apt-get autoremove -y && rm
-rf /tmp/* /var/lib/apt/lists/* &&\  
useradd -m teams && mkdir /teams-for-linux && chown teams:teams /teams-for-
linux  
USER teams  
ENTRYPOINT [ "teams" ]  

