FROM kpmeen/docker-scala-sbt  
  
# set ClamAV version to use  
ENV AV_VERSION 0.99.2  
# initial install of av daemon needs package repositories  
RUN echo "deb http://http.debian.net/debian/ jessie main contrib non-free" >
/etc/apt/sources.list && \  
echo "deb http://http.debian.net/debian/ jessie-updates main contrib non-free"
>> /etc/apt/sources.list && \  
echo "deb http://security.debian.org/ jessie/updates main contrib non-free" >>
/etc/apt/sources.list  
  
RUN apt-get update  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
-qq \  
clamav-daemon=${AV_VERSION}* \  
clamav-freshclam=${AV_VERSION}* \  
libclamunrar7 \  
apt-utils \  
curl  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# initial update of AV databases  
RUN curl -L -o /var/lib/clamav/main.cvd http://database.clamav.net/main.cvd &&
\  
curl -L -o /var/lib/clamav/daily.cvd http://database.clamav.net/daily.cvd && \  
curl -L -o /var/lib/clamav/bytecode.cvd
http://database.clamav.net/bytecode.cvd  
  
RUN chown clamav:clamav /var/lib/clamav/*.cvd  
  
# permission juggling  
RUN mkdir /var/run/clamav && \  
chown clamav:clamav /var/run/clamav && \  
chmod 750 /var/run/clamav  
  
# av configuration update  
RUN sed -i 's/^Foreground .*$/Foreground true/g' /etc/clamav/clamd.conf && \  
echo "TCPSocket 3310" >> /etc/clamav/clamd.conf && \  
sed -i 's/^StreamMaxLength 25M$/StreamMaxLength 2M/g' /etc/clamav/clamd.conf
&& \  
sed -i 's/^Foreground .*$/Foreground true/g' /etc/clamav/freshclam.conf  
  
# volume provision  
VOLUME ["/var/lib/clamav"]  
  
# port provision  
EXPOSE 3310  
# Define working directory  
WORKDIR /root  
  
# av daemon bootstrapping  
ADD bootstrap.sh /  
CMD ["/bootstrap.sh"]  

