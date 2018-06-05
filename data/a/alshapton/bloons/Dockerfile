FROM alpine:latest  
MAINTAINER "admin@vbloons.com"  
# Install Python and the corresponding frameworks  
#RUN apk add python python-dev py-pip build-base  
RUN apk add --update \  
python \  
python-dev \  
py-pip \  
build-base \  
jpeg-dev \  
zlib-dev \  
&& pip install virtualenv \  
&& ln -s /usr/include/locale.h /usr/include/xlocale.h \  
&& rm -rf /var/cache/apk/*  
# Note the xlocale.x fix above.... for Alpine Linux to allow numpy to work
correctly  
# Note the fix for zlib for Alpine linux  
ENV LIBRARY_PATH=/lib:/usr/lib  
  
RUN pip install --upgrade pip  
  
#RUN yes | apk add python-pip && \  
RUN pip install Django  
RUN pip install numpy  
RUN pip install Pillow  
  
#Install the AWS libraries  
RUN pip install boto  
RUN pip install boto3  
  
# Install the Stripe payment library  
RUN pip install stripe  
  
#Install latest code  
RUN mkdir bloons  
WORKDIR bloons  
  
ADD platform/ platform  
ADD Bloons/ Bloons  
ADD BloonsWeb/ BloonsWeb  
ADD appspec.yml .  
ADD README.md .  
  
# Set up AWS credentials - ensure that they are in the correct working
directory  
WORKDIR /root  
RUN mkdir .aws  
RUN cp /bloons/platform/credentials ./.aws  
  
# Port 7999 is exposed for the webserver  
EXPOSE 7999  
#Command to use when the container is started  
CMD /bloons/BloonsWeb/manage/startserverLocalDocker.sh  
  
# Removed GIT reduced Imge from 927Mb to 899Mb  
# Colapsed Python/Django into one line no change in Image size  
# Changed from Linux-Mint to Alpine Linux reduced Image from 899Mb to 329Mb

