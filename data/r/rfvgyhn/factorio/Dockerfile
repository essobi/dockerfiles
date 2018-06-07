FROM frolvlad/alpine-glibc:alpine-3.5  
RUN apk --no-cache add tini  
ENTRYPOINT ["/sbin/tini", "--"]  
  
ENV VERSION=0.16.47  
RUN apk --no-cache add curl pwgen  
RUN mkdir -p /opt /saves  
RUN curl -LSs https://www.factorio.com/get-
download/${VERSION}/headless/linux64 | tar -xJC /opt  
RUN ln -s /saves /opt/factorio/saves  
RUN apk --no-cache del curl  
  
COPY files /  
RUN chmod +x /usr/local/bin/factorio  
  
VOLUME /saves  
VOLUME /mods  
VOLUME /config  
  
# RCON  
EXPOSE 27015/udp  
  
# Game  
EXPOSE 34197/udp  
  
  
ENV FACTORIO_SAVE_NAME=meeseeks  
ENV FACTORIO_PORT=  
ENV FACTORIO_BIND_ADDRESS=  
ENV FACTORIO_SCENARIO=  
  
CMD ["/run.sh"]

