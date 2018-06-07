FROM ubuntu:xenial  
MAINTAINER Andrey Arapov <andrey.arapov@nixaid.com>  
  
# To avoid problems with Dialog and curses wizards  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get -y --no-install-recommends install \  
ca-certificates apt-transport-https gnupg  
  
ADD https://atlassian.artifactoryonline.com/atlassian/api/gpg/key/public \  
/tmp/public  
RUN cat /tmp/public | apt-key add - && \  
echo "deb https://atlassian.artifactoryonline.com/atlassian/hipchat-apt-client
xenial main" > /etc/apt/sources.list.d/atlassian-hipchat4.list  
RUN apt-get update  
RUN apt-get -y --no-install-recommends install hipchat4 libqt5gui5  
RUN apt-get -fy --no-install-recommends install  
  
RUN useradd -u 1000 -m -d /home/user -s /usr/sbin/nologin -g video user  
  
WORKDIR /home/user  
VOLUME [ "/tmp" ]  
USER user  
ENTRYPOINT [ "/usr/local/bin/hipchat4" ]  

