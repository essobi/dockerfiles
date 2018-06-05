FROM phusion/baseimage:0.9.16  
CMD ["/sbin/my_init"]  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV GDK_BACKEND broadway  
ENV UBUNTU_MENUPROXY 0  
ENV LIBOVERLAY_SCROLLBAR 0  
RUN sudo apt-get -qqy upgrade && sudo apt-get -qqy install python3-software-
properties software-properties-common && \  
add-apt-repository -y ppa:malizor/gtk-broadway && sudo apt-get -qq update && \  
sudo apt-get -qqy upgrade && sudo apt-get -qqy install broadwayd
gtk-3-examples  
  
RUN mkdir /etc/service/broadway  
ADD broadway.sh /etc/service/broadway/run  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# run  
# docker run --rm -ti -p 127.0.0.1:8080:8080 gtk3new /sbin/my_init --
gtk3-demo  

