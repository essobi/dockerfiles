# Docker image for OE-lite.org buildbot slave  
FROM docker:1.12  
MAINTAINER Esben Haabendal <esben@haabendal.dk>  
  
# Install various needed packages  
RUN apk add --no-cache --progress \  
python python-dev build-base \  
libffi-dev openssl-dev \  
git sudo \  
&& rm -rf /var/cache/apk/*  
  
# Install Python pip  
RUN wget "https://bootstrap.pypa.io/get-pip.py" -O /dev/stdout | python \  
&& pip install --upgrade pip  
  
# Install buildbot itself and pip dependencies  
RUN pip install buildbot-slave  
  
# Install setup and start scripts and buildbot configuration  
COPY assets /srv/setup/  
  
# Setup buildbot user  
#RUN addgroup -S -g 667 buildbot \  
# && adduser -S -D -u 667 -G buildbot -h /srv/buildbot -s /bin/bash buildbot \  
# && chown -R buildbot:buildbot /srv/setup  
RUN adduser -D -h /srv/buildbot -s /bin/bash buildbot \  
&& chown -R buildbot:buildbot /srv/setup  
  
WORKDIR /srv/buildbot  
  
# Setup whatever is possible to do at image build time (not much...)  
RUN /srv/setup/setup.sh  
  
CMD ["./start.sh"]  

