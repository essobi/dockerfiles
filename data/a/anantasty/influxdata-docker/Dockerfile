FROM buildpack-deps:trusty-curl  
  
RUN gpg \  
\--keyserver hkp://ha.pool.sks-keyservers.net \  
\--recv-keys 05CE15085FC09D18E99EFB22684A14CF2582E0C5  
  
ENV TELEGRAF_VERSION 1.1.1  
RUN wget -q
https://dl.influxdata.com/telegraf/releases/telegraf_${TELEGRAF_VERSION}_amd64.deb.asc
&& \  
wget -q
https://dl.influxdata.com/telegraf/releases/telegraf_${TELEGRAF_VERSION}_amd64.deb
&& \  
gpg --batch --verify telegraf_${TELEGRAF_VERSION}_amd64.deb.asc
telegraf_${TELEGRAF_VERSION}_amd64.deb && \  
dpkg -i telegraf_${TELEGRAF_VERSION}_amd64.deb && \  
rm -f telegraf_${TELEGRAF_VERSION}_amd64.deb*  
  
RUN wget -q https://raw.githubusercontent.com/tests-always-
included/mo/master/mo  
RUN mv mo /usr/local/bin &&\  
chmod +x /usr/local/bin/mo  
  
EXPOSE 8125/udp 8092/udp 8094  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["telegraf"]  

