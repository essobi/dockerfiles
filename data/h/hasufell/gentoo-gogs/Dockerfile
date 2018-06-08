FROM hasufell/gentoo-amd64-paludis:latest  
MAINTAINER Julian Ospald <hasufell@gentoo.org>  
  
  
##### PACKAGE INSTALLATION #####  
# copy paludis config  
COPY ./config/paludis /etc/paludis  
  
# update world with our USE flags  
RUN chgrp paludisbuild /dev/tty && cave resolve -c world -x  
  
# install gogs dependencies  
RUN chgrp paludisbuild /dev/tty && cave resolve -c gogs -x  
  
# install tools set  
RUN chgrp paludisbuild /dev/tty && cave resolve -c tools -x  
  
# update etc files... hope this doesn't screw up  
RUN etc-update --automode -5  
  
################################  
ENV GOPATH /gopath  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  
  
WORKDIR /gopath/src/github.com/gogits/gogs/  
RUN git clone \--depth=1 https://github.com/gogits/gogs.git \  
/gopath/src/github.com/gogits/gogs  
  
# Build binary and clean up useless files  
RUN go get -v -tags "sqlite redis memcache cert pam" && \  
go build -tags "sqlite redis memcache cert pam" && \  
mkdir /app/ && \  
mv /gopath/src/github.com/gogits/gogs/ /app/gogs/ && \  
rm -r "$GOPATH"  
  
WORKDIR /app/gogs/  
  
RUN useradd --shell /bin/bash --system --comment gogits git  
  
# SSH login fix, otherwise user is kicked off after login  
RUN echo "export VISIBLE=now" >> /etc/profile && \  
echo "PermitUserEnvironment yes" >> /etc/ssh/sshd_config  
  
# Setup server keys on startup  
RUN echo "HostKey /data/ssh/ssh_host_rsa_key" >> /etc/ssh/sshd_config && \  
echo "HostKey /data/ssh/ssh_host_dsa_key" >> /etc/ssh/sshd_config && \  
echo "HostKey /data/ssh/ssh_host_ed25519_key" >> /etc/ssh/sshd_config  
  
# Prepare data  
ENV GOGS_CUSTOM /data/gogs  
RUN echo "export GOGS_CUSTOM=/data/gogs" >> /etc/profile  
  
COPY setup.sh /setup.sh  
RUN chmod +x /setup.sh  
COPY config/supervisord.conf /etc/supervisord.conf  
  
EXPOSE 3000  
CMD /setup.sh && exec /usr/bin/supervisord -n -c /etc/supervisord.conf  

