FROM frolvlad/alpine-glibc:alpine-3.5_glibc-2.25  
LABEL maintainer="DerEnderKeks <admin@derenderkeks.me>" description="Docker
image for factorio servers"  
  
WORKDIR /srv/factorio  
ENV SERVER /srv/factorio/bin/x64/factorio  
ENV CONFIG /srv/factorio/config/server-settings.json  
ENV WHITELIST /srv/factorio/config/server-whitelist.json  
ENV BANLIST /srv/factorio/config/server-banlist.json  
  
RUN apk add --update-cache curl tar xz  
  
RUN curl -sL https://www.factorio.com/get-download/stable/headless/linux64 |
tar --strip-components=1 -xJ  
  
COPY . /srv/factorio/  
  
EXPOSE 34197/udp  
VOLUME /srv/factorio/config /srv/factorio/saves /srv/factorio/mods  
  
CMD ["sh", "./start.sh"]  

