# ciphrtxt-test  
FROM jadeblaquiere/ciphrtxt-base-os  
  
# TODO: Put the maintainer name in the image metadata  
MAINTAINER Joseph deBlaquiere <jadeblaquiere@yahoo.com>  
  
# TODO: Rename the builder environment variable to inform users about
application you provide them  
ENV BUILDER_VERSION 0.1  
ENV COINSVC_USERNAME rpcuser  
ENV COINSVC_PASSWORD rpcpass  
ENV COINSVC_HOST coinsvc  
ENV COINSVC_RPCPORT 7765  
ENV EXTHOSTNAME localhost  
ENV NAKPRIV "0000000000000000000000000000000000000000000000000000000000000000"  
EXPOSE 7754  
# install msgstore  
RUN (cd /home/ciphrtxt && git clone
https://github.com/jadeblaquiere/msgstore.git)  
  
RUN echo "#!/usr/bin/env sh" > /home/ciphrtxt/run.sh  
RUN echo "if [ \$EXTHOSTNAME = \"localhost\" ] && [
\$DOCKERCLOUD_CONTAINER_FQDN != \"\" ] ; then export
EXTHOSTNAME=\$DOCKERCLOUD_CONTAINER_FQDN ; fi" >> /home/ciphrtxt/run.sh  
RUN echo "(cd /home/ciphrtxt/msgstore && python3 ./app.py
--rpcuser=\$COINSVC_USERNAME --rpcpass=\$COINSVC_PASSWORD
--coinhost=\$COINSVC_HOST --coinport=\$COINSVC_RPCPORT --exthost=\$EXTHOSTNAME
--nakpriv=\$NAKPRIV)" >> /home/ciphrtxt/run.sh  
  
RUN chmod 755 /home/ciphrtxt/run.sh  
  
CMD /home/ciphrtxt/run.sh  

