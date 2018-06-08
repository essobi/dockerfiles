FROM python:3-alpine as builder  
MAINTAINER Laurent Corbes <caf@glot.net>  
  
ENV GANDICLIVER latest  
  
# install base tools and build gandi.cli  
RUN apk --no-cache add \  
git \  
gcc libc-dev \  
yaml-dev \  
&& BUILD=`mktemp -d` \  
&& git clone \--depth 1 https://github.com/Gandi/gandi.cli.git $BUILD \  
&& cd $BUILD \  
&& mkdir -p /tmp/local/lib/python3.6/site-packages/ \  
&& export PYTHONPATH=/tmp/local/lib/python3.6/site-packages/ \  
&& python setup.py install --prefix /tmp/local  
  
FROM python:3-alpine  
# get installed packages from builder stage  
COPY \--from=builder /tmp/local/ /usr/local/  
# install ssh client binary needed by some commands  
RUN apk --no-cache add openssh-client  
  
WORKDIR /root/  
ADD profile .profile  
  
VOLUME ["/root/.config/gandi"]  
  
#ENTRYPOINT ["/usr/local/bin/gandi"]  
CMD ["/bin/sh", "--login"]  

