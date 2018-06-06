FROM alpine:latest  
  
ENV LANG='en_US.UTF-8'  
ENV LANGUAGE='en_US:en'  
ENV LC_ALL='en_US.UTF-8'  
LABEL tags="latest 1.0.2" \  
build_ver="19-06-2018"  
  
WORKDIR /root/centerim5  
  
RUN apk --no-cache add \  
git libtool gettext-libs gettext-dev pidgin-dev libsigc++ libsigc++-dev \  
python3 autoconf g++ ncurses-dev gettext automake make libpurple \  
libpurple-oscar libpurple-xmpp libpurple-bonjour ncurses openssh-client \  
&& rm -rf /var/cache/apk/*  
  
RUN cd /root && mkdir -p ~/.ssh && ssh-keyscan -H repo.or.cz >>
~/.ssh/known_hosts \  
&& git clone -b mob git+ssh://mob@repo.or.cz/srv/git/centerim5.git && cd
/root/centerim5 \  
&& ./bootstrap && ./configure && make && make install && rm -rf
/root/centerim5  
  
CMD ["/usr/local/bin/centerim5"]

