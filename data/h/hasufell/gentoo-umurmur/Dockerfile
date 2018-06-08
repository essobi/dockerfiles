FROM hasufell/gentoo-amd64-paludis:latest  
MAINTAINER Julian Ospald <hasufell@gentoo.org>  
  
##### PACKAGE INSTALLATION #####  
# copy paludis config  
COPY ./config/paludis /etc/paludis  
  
# update world with our USE flags  
RUN chgrp paludisbuild /dev/tty && cave resolve -c world -x  
  
# install umurmurset set  
RUN chgrp paludisbuild /dev/tty && cave resolve -c umurmurset -x  
  
# install tools set  
RUN chgrp paludisbuild /dev/tty && cave resolve -c tools -x  
  
# update etc files... hope this doesn't screw up  
RUN etc-update --automode -5  
  
################################  
COPY ./config/umurmur.conf /etc/umurmur/umurmur.conf  
RUN mkdir /umurmurconfig  
COPY ./config/channels.conf /umurmurconfig/  
  
COPY ./setup.sh /setup.sh  
RUN chmod +x /setup.sh  
COPY ./config/supervisord.conf /etc/supervisord.conf  
  
EXPOSE 64738  
CMD /setup.sh && exec /usr/bin/supervisord -n -c /etc/supervisord.conf  

