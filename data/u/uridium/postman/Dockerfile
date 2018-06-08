FROM debian:stretch-slim  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ARG UID=1000  
ARG GID=1000  
RUN apt-get update -qq \  
&& apt-get dist-upgrade -y -qq \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
libasound2 \  
libgconf2-4 \  
libgtk2.0-0 \  
libnss3 \  
libx11-xcb1 \  
libxss1 \  
libxtst6 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*  
  
RUN cd /usr/local \  
&& curl -sL http://dl.pstmn.io/download/latest/linux64 -o postman.tar.gz \  
&& tar xf postman.tar.gz \  
&& rm -f postman.tar.gz  
  
RUN groupadd -g $UID postman \  
&& useradd -m -u $UID -g postman postman  
  
USER postman  
  
ENTRYPOINT ["/usr/local/Postman/Postman"]  

