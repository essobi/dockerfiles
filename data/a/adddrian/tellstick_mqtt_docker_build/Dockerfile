FROM ubuntu:14.04  
RUN apt-get update -y && \  
apt-get dist-upgrade -y && \  
sh -c 'echo "deb http://download.telldus.com/debian/ stable main" >>
/etc/apt/sources.list' && \  
apt-key adv --fetch-keys http://download.telldus.se/debian/telldus-public.key
&& \  
apt-get update -y && \  
apt-get install -y telldus-core libftdi1 && \  
/etc/init.d/telldusd start  
  
RUN apt-get update -y && \  
apt-get install python-pip python-dev build-essential -y && \  
pip install --upgrade pip && \  
pip install --upgrade virtualenv && \  
pip install tellcore-py  
  
RUN pip install paho-mqtt  
  
RUN apt-get install libyaml-dev -y && \  
pip install ruamel.yaml  
  
RUN sed -i -- 's/nobody/root/g' /etc/tellstick.conf && \  
sed -i -- 's/plugdev/root/g' /etc/tellstick.conf  
  
COPY tellstickService.py /tellstick/tellstickService.py  
COPY config.yaml /tellstick/config.yaml  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD /etc/init.d/telldusd start && python -u /tellstick/tellstickService.py  

