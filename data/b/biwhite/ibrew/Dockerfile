FROM alpine:latest  
MAINTAINER Ben White <ben@cuckoo.org>  
RUN apk update && apk add bash avahi-tools avahi-compat-libdns_sd screen
python git py-tornado  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.18.1.5/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
ADD root /  
WORKDIR /home/app  
RUN wget
http://groups.csail.mit.edu/o2s/download/pybonjour/pybonjour-1.1.1.tar.gz  
RUN tar -zxf pybonjour-1.1.1.tar.gz  
RUN cd pybonjour-1.1.1 && /usr/bin/python setup.py install  
RUN git clone https://github.com/Tristan79/iBrew.git  
#RUN sed -i 's/x = raw_input("")/time.sleep(60)/' iBrew/iBrewConsole.py  
VOLUME /var/run/dbus/system_bus_socket  
EXPOSE 2080  
ENTRYPOINT ["/init"]  

