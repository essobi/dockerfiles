FROM selenium/standalone-firefox-debug  
MAINTAINER albert alvarez  
  
EXPOSE 7000 5000  
RUN mkdir /usr/lib/firefox-addons  
RUN mkdir /usr/lib/firefox-addons/extensions  
COPY extensions/ /root/.mozilla/extensions  
COPY extensions/ /usr/lib/firefox-addons/extensions  
  
  
RUN wget -O /usr/local/sbin/install-mozilla-addon
http://bernaerts.dyndns.org/download/ubuntu/install-mozilla-addon  
RUN chmod +x /usr/local/sbin/install-mozilla-addon  
  
RUN install-mozilla-addon /root/.mozilla/extensions/foxyproxy.xpi  
RUN install-mozilla-addon /usr/lib/firefox-addons/extensions/foxyproxy.xpi  
#RUN sed -i 's/wait $NODE_PID/firefox -silent -install-global-extension
\/home\/foxyproxy.xpi \&\& wait $NODE_PID/g' /opt/bin/entry_point.sh  
##CMD ["firefox","-silent","-install-global-extension selenium-
expert_selenium-ide@Samit.Badle.xpi","-setDefaultBrowser","www.google.es"]  

