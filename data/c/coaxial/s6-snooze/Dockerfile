FROM coaxial/s6-base  
  
# install snooze  
ARG SNOOZE_DEPS="make gcc musl-dev"  
RUN apk \--no-cache add curl &&\  
curl -L https://api.github.com/repos/chneukirchen/snooze/tarball/master -o
/tmp/snooze.tar.gz &&\  
mkdir /tmp/snooze &&\  
tar xzf /tmp/snooze.tar.gz -C /tmp/snooze \--strip 1 &&\  
cd /tmp/snooze &&\  
apk \--no-cache add $SNOOZE_DEPS &&\  
make install &&\  
rm -rf /tmp/snooze &&\  
rm -rf /tmp/snooze.tar.gz &&\  
apk \--no-cache del $SNOOZE_DEPS  
  
ENTRYPOINT ["/init"]  

