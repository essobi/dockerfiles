FROM debian:latest  
  
MAINTAINER Sergio Tejón <sergio.tejon@gmail.com>  
  
ADD ./src /src  
WORKDIR /src/tg  
  
RUN apt-get update && apt-get -y install libreadline-dev libconfig-dev libssl-
dev lua5.2 liblua5.2-dev libevent-dev libjansson-dev libpython-dev build-
essential && \  
./configure && \  
make  
  
RUN useradd telegramd && \  
mkdir /usr/share/telegram-daemon && \  
mkdir /usr/share/telegram-daemon/bin && \  
cp bin/telegram-cli /usr/share/telegram-daemon/bin/ && \  
mkdir /etc/telegram-cli && \  
cp server.pub /etc/telegram-cli/server.pub  
  
RUN apt-get purge -y --auto-remove build-essential  
  
ADD ./etc/telegram.conf /etc/telegram-cli  
  
EXPOSE 2391  
CMD [ "/usr/share/telegram-daemon/bin/telegram-cli", "-vvvvR", "-k",
"/etc/telegram-cli/server.pub", "-W", "-d", "-P", "2391", "--accept-any-tcp",
"-c", "/etc/telegram-cli/telegram.conf", "$OUTPUT_MODE" ]  
  

