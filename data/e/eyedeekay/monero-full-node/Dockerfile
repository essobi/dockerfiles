# Usage: docker run -d --cap-drop all -v $HOME/blockchain-
xmr:/home/xmrdaemon/.bitmonero --network=host --name=monerod -td monero-full-
node  
FROM debian:sid  
ARG hash  
ARG iface  
ARG daemon_host  
ARG daemon_port  
ENV daemon_host=127.0.0.1 daemon_port=18081 iface=$iface  
RUN apt-get update  
RUN apt-get install -y bzip2 wget  
RUN adduser --disabled-password --gecos '' \--home /home/xmrdaemon xmrdaemon  
  
WORKDIR /home/xmrdaemon  
  
RUN wget https://downloads.getmonero.org/$iface/linux64 && \  
echo "$hash linux64" | sha256sum -c - && \  
tar jxvf linux64 && \  
rm linux64  
  
RUN chmod a+x monero*/*  
  
RUN chown -R xmrdaemon:xmrdaemon /home/xmrdaemon  
  
USER xmrdaemon  
  
# blockchain loaction  
VOLUME /home/xmrdaemon/.bitmonero  
  
EXPOSE 18080 18081  
CMD /home/xmrdaemon/monero-v0.12.0.0/monerod \  
\--restricted-rpc \  
\--rpc-bind-ip=0.0.0.0 \  
\--confirm-external-bind  

