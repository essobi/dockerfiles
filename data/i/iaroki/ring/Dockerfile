FROM debian:stretch  
MAINTAINER iaroki  
RUN apt-get update && apt-get install apt-transport-https dirmngr -y \  
&& sh -c "echo 'deb https://dl.ring.cx/ring-nightly/debian_9/ ring main' >
/etc/apt/sources.list.d/ring-nightly-man.list" \  
&& apt-key adv --keyserver pgp.mit.edu --recv-keys
A295D773307D25A33AE72F2F64CD5FA175348F84 \  
&& apt-get update && apt-get install ring dbus-x11 -y && apt-get clean  
RUN useradd -m -u 1000 -G audio,video iaroki  
USER iaroki  
WORKDIR /home/iaroki  
CMD ["gnome-ring"]  

