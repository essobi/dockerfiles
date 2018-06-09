# docker run --rm -it \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY=$DISPLAY \  
# --name toggl \  
# webcoreit/toggl  
  
FROM webcoreit/debian:graphical  
  
MAINTAINER Tom <info@webcore-it.com>  
  
# Install toggl (download the latest version)  
RUN curl -sSL -o /tmp/toggl.tar.gz
"https://toggl.com/api/v8/installer?app=td&platform=linux&channel=stable" \  
&& mkdir -p /usr/src/toggl \  
&& tar -xf /tmp/toggl.tar.gz -C /usr/src/toggl --strip-components 1 \  
&& rm -rf /tmp/toggl.tar.gz \  
&& chown -R root:root /usr/src/toggl  
  
# Tell toggl the path to it's lib  
ENV LD_LIBRARY_PATH /usr/src/toggl/lib  
# Run toggl  
CMD ["/usr/src/toggl/TogglDesktop"]

