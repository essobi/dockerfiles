FROM ubuntu:trusty  
MAINTAINER Tanapong <tanapong.prince@gmail.com>  
  
# Prevent dpkg errors  
ENV TERM=xterm-256color  
  
# Install Package runtime  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
build-essential \  
ca-certificates \  
gcc \  
git \  
libpq-dev \  
make \  
mercurial \  
pkg-config \  
python3 \  
python3-dev \  
python3-pip \  
python-virtualenv \  
ssh \  
&& apt-get autoremove \  
&& apt-get clean  
  
# Run virtualenv  
RUN virtualenv -p python3 /appenv && \  
. /appenv/bin/activate && \  
pip3 install pip --upgrade  
  
# Add entrypoint script  
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["entrypoint.sh"]  
  
LABEL application=todobackend

