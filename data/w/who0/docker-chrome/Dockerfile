FROM debian  
  
ENV Usr=chrome  
RUN apt-get update  
RUN apt-get install -qy chromium  
RUN apt-get install -qy libpulse0 mpg123  
RUN useradd $Usr -s /bin/bash -d /$Usr && mkdir /$Usr && chown $Usr -R /$Usr  
RUN echo "#!/bin/bash\nchromium --no-sandbox" >> /script.sh && chmod a+x
script.sh  
ENV PULSE_SERVER=unix:/var/run/pulse/native  
USER $Usr  
  
ENTRYPOINT /script.sh  
  
  
# docker run -it --rm  
# -v /run/user/$UID/pulse/native:/var/run/pulse/native  
# -v /tmp/.X11-unix:/tmp/.X11-unix  
# -v chrome:/chrome/.config/chromium  
# -e DISPLAY=unix$DISPLAY who0/docker-chrome  

