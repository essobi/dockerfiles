FROM debian:jessie  
  
RUN apt-get update && apt-get install wget curl -y  
ARG MOPDIY_VERSION=2.1.0-1  
# Dependencyies for mopidy base  
RUN wget -q -O - https://apt.mopidy.com/mopidy.gpg | apt-key add -  
RUN wget -q -O /etc/apt/sources.list.d/mopidy.list
https://apt.mopidy.com/jessie.list  
  
RUN apt-get update && apt-get install mopidy=${MOPDIY_VERSION} mopidy-dleyna
-y  
  
RUN curl -L https://bootstrap.pypa.io/get-pip.py | python  
RUN pip install Mopidy-Moped --upgrade  
RUN pip install Mopidy-dLeyna --upgrade  
RUN pip install mopidy-musicbox-webclient --upgrade  
  
# Default configuration  
ADD mopidy.conf /var/lib/mopidy/.config/mopidy/mopidy.conf  
  
RUN chown mopidy:audio -R /var/lib/mopidy/.config  
# Run as mopidy user  
USER mopidy  
  
VOLUME /var/lib/mopidy/local  
VOLUME /var/lib/mopidy/media  
  
EXPOSE 6600  
EXPOSE 6680  
  
CMD ["/usr/bin/mopidy"]  

