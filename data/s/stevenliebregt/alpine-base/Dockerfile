FROM alpine:3.5  
MAINTAINER Steven Liebregt <dev.s.liebregt@gmail.com>  
  
RUN echo "@community http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
  
# Update and install packages  
apk update && apk upgrade && \  
apk add ca-certificates rsyslog logrotate runit && \  
apk add nano vim git python python3 && \  
apk add curl && \  
  
# Install utils and init process  
cd /tmp && \  
curl -Ls https://github.com/StevenLiebregt/docker-utils/archive/master.tar.gz
| tar xfz - && \  
./docker-utils-master/install.sh && \  
rm -Rf ./docker-utils-master && \  
  
# Fix container bug for syslog  
sed -i "s|\\*.emerg|\\#\\*.emerg|" /etc/rsyslog.conf && \  
sed -i 's/$ModLoad imklog/#$ModLoad imklog/' /etc/rsyslog.conf && \  
sed -i 's/$KLogPermitNonKernelFacility on/#$KLogPermitNonKernelFacility on/'
/etc/rsyslog.conf && \  
  
# Remove cached info  
rm -rf /var/cache/apk/*  
  
# Set environment variables  
ENV HOME /root  
  
# Define working directory  
WORKDIR /root  
  
# Define default command  
CMD ["/boot.sh"]  

