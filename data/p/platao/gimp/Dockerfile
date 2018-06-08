# Run container in Desktop:  
# xhost +local:docker;  
# docker run --rm --name gimp \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -v ~/Desktop:/home \  
# -e DISPLAY \  
# platao/gimp;  
# xhost -local:docker;  
FROM alpine  
  
ENV app=gimp home=/home user=gimpuser uid=1000  
  
RUN adduser -h $home -s /sbin/nologin -u $uid -D $user && \  
apk add \--no-cache \  
dbus-x11 \  
dumb-init \  
gimp \  
mesa-gl \  
ttf-freefont  
  
USER  $user  
WORKDIR $home  
  
ENTRYPOINT ["gimp"]  

