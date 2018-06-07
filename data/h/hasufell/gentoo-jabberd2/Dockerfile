FROM hasufell/gentoo-amd64-paludis:latest  
MAINTAINER Julian Ospald <hasufell@gentoo.org>  
  
##### PACKAGE INSTALLATION #####  
# copy paludis config  
COPY ./config/paludis /etc/paludis  
  
# update world with our USE flags  
RUN chgrp paludisbuild /dev/tty && cave resolve -c world -x  
  
# install jabberd2 set  
RUN chgrp paludisbuild /dev/tty && cave resolve -c jabberd2set -x  
  
# install tools set  
RUN chgrp paludisbuild /dev/tty && cave resolve -c tools -x  
  
# update etc files... hope this doesn't screw up  
RUN etc-update --automode -5  
  
################################  
COPY ./config/supervisord.conf /etc/supervisord.conf  
  
EXPOSE 5222 5223 5269  
CMD exec /usr/bin/supervisord -n -c /etc/supervisord.conf  

