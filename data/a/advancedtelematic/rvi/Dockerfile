FROM debian:jessie  
  
RUN apt-get update && \  
apt-get install -y libbluetooth3 bluez python-jsonrpclib wget  
  
RUN echo "deb http://packages.erlang-solutions.com/debian jessie contrib" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y --force-yes esl-erlang  
  
WORKDIR /opt  
RUN wget
https://github.com/PDXostc/rvi_core/releases/download/v0.5.0/rvi_0.5.0-1_amd64.deb
&& \  
dpkg -i rvi_0.5.0-1_amd64.deb  
  
COPY backend.rvi.config /etc/rvi/  
COPY device.rvi.config /etc/rvi/  
COPY run_rvi.sh /usr/bin/run_rvi.sh  
  
ENTRYPOINT ["/usr/bin/run_rvi.sh"]  
CMD ["backend"]  

