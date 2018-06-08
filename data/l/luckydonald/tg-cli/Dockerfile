FROM debian:8.6  
  
RUN useradd telegram && mkdir -p /home/telegram/.telegram-cli/ && chown
telegram /home/telegram/.telegram-cli  
  
ENV TGCLI_VERSION 1124  
  
# This could be even smaller if we disable Python (there's a bug preventing
the configure flag from working currently)  
RUN apt-get update -y && apt-get install -y libreadline-dev libconfig-dev
libssl-dev lua5.2 liblua5.2-dev libevent-dev libjansson-dev \  
libpython-dev make libbsd0 curl && \  
curl -L "https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-
init_1.1.3_amd64" -o /bin/dumb-init && \  
curl -L "https://valtman.name/files/telegram-cli-${TGCLI_VERSION}" -o
/bin/telegram-cli && \  
chmod +x /bin/dumb-init /bin/telegram-cli && \  
apt-get purge -y ca-certificates curl && apt-get autoremove -y && apt-get
clean my room  
  
WORKDIR /home/telegram  
  
ADD ./configfile.txt /telegram/config  
RUN mkdir -p /telegram/data/data && chmod -R 777 /telegram/data  
  
# USER telegram  
  
EXPOSE 4458  
  
ENTRYPOINT ["/bin/dumb-init", "--"]  
  
CMD ["/bin/telegram-cli", "--json", "-P", "4458", "--accept-any-tcp", "--
disable-readline", "--config", "/telegram/config"]

