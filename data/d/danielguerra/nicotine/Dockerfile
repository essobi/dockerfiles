FROM ubuntu:14.04  
MAINTAINER Daniel Guerra  
RUN apt-get -yy update \  
&& apt-get -yq install libx11-6 libx11-xcb1 libfontconfig1 supervisor xvfb
x11vnc openbox nicotine \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN addgroup nicotine  
RUN useradd -s /bin/bash -m -g nicotine nicotine  
RUN echo "nicotine:nicotine" | /usr/sbin/chpasswd  
RUN echo "nicotine ALL=(ALL) ALL" >> /etc/sudoers  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN touch /var/log/supervisor/supervisord.log  
RUN chown -R nicotine:nicotine /var/log/supervisor/  
WORKDIR /home/nicotine  
USER nicotine  
EXPOSE 5900  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

