# Run CoyIM - XMPP Client  
# docker run --name coyim \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY=unix$DISPLAY \  
# --rm c0dy/coyim  
FROM golang:stretch  
LABEL maintainer "Cody Zacharias <codyzacharias@pm.me>"  
  
# Install Packages  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y tor \  
gtk+3.0 \  
libgtk-3-dev  
  
# Create non-priv user  
RUN adduser --disabled-password --shell /bin/sh coy  
  
# Install CoyIM  
RUN export GTK_VERSION=$(pkg-config --modversion gtk+-3.0 | tr . _ | cut -d
'_' -f 1-2) && \  
go get -u -tags "gtk_${GTK_VERSION}" github.com/coyim/coyim  
  
ENV PATH="${PATH}:/go/bin"  
# Run as non-priv user  
USER coy  
  
# Start CoyIM w/ Tor  
RUN echo "#!/bin/sh" >> run.sh && \  
echo "nohup sh -c tor &" >> run.sh && \  
echo "coyim" >> run.sh && \  
chmod 775 run.sh  
  
CMD ["./run.sh"]  

