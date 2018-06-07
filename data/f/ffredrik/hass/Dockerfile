#FROM taskinen/home-assistant:latest # Lots copied from this dockerfile  
FROM homeassistant/home-assistant:latest  
MAINTAINER Fredrik Fjeld <fredrik@fjeld.io>  
  
# Add Telldus repository  
RUN echo "deb-src http://download.telldus.com/debian/ unstable main" >>
/etc/apt/sources.list.d/telldus.list  
RUN curl -sSL http://download.telldus.com/debian/telldus-public.key | apt-key
add -  
  
# Install dependencies. Compile and install telldusd  
RUN apt-get update  
RUN apt-get install -y build-essential  
RUN apt-get build-dep -y telldus-core  
RUN apt-get install -y cmake libconfuse-dev libftdi-dev help2man  
RUN apt-get --compile source telldus-core  
RUN dpkg --install *.deb  
  
# Install and configure Supervisor  
RUN apt-get install -y supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ENTRYPOINT
["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]  
  
# Install dependencies for the new Z-Wave update required since 0.45  
RUN apt-get install -y libudev-dev  
  
# Install dependencies for IKEA Trådfri  
RUN apt-get update  
RUN apt-get install -y libtool autoconf git-core  
RUN git clone \--depth 1 --recursive -b dtls https://github.com/home-
assistant/libcoap.git  
RUN cd libcoap && ./autogen.sh && ./configure --disable-documentation
--disable-shared --without-debug CFLAGS="-D COAP_DEBUG_FD=stderr" && make &&
make install  
  
# Install dependencies for Apple TV  
RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev
python3-setuptools python3-dev  
  
# Install dependencies for Bluetooth LE  
RUN apt-get install -y python3-pip libglib2.0-dev  
RUN pip3 install bluepy  
  
# Clean up  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Specify health check for Docker  
HEALTHCHECK CMD curl --fail http://localhost:8123 || exit 1  
  

