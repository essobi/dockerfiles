FROM phusion/baseimage:0.9.22  
MAINTAINER Sebastian Fialka <sebastian.fialka@sebfia.net>  
  
CMD ["/sbin/my_init"]  
# install xvfb and other X dependencies  
RUN apt-get update -y \  
&& apt-get install -y wget xvfb libxrender1 libxtst6 x11vnc \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /tmp  
RUN wget https://download2.interactivebrokers.com/installers/ibgateway/stable-
standalone/ibgateway-stable-standalone-linux-x64.sh && \  
# wget https://download2.interactivebrokers.com/installers/ibgateway/latest-
standalone/ibgateway-latest-standalone-linux-x64.sh &&\  
chmod a+x *.sh && \  
echo "n" | ./ibgateway-stable-standalone-linux-x64.sh && \  
rm -rf /tmp/*  
  
COPY init/xvfb_init /etc/init.d/xvfb  
COPY init/vnc_init /etc/init.d/vnc  
# RUN mkdir /etc/service/xvfb  
COPY bin/xvfb-daemon-run /usr/bin/xvfb-daemon-run  
#RUN chmod a+x /etc/service/xvfb/run  
COPY bin/run-installer /usr/bin/run-installer  
  
EXPOSE 5900  
ENV DISPLAY :0  
CMD ["/usr/bin/run-installer"]  

