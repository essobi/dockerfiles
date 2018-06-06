FROM debian:stretch  
MAINTAINER Markos Chandras <hwoarang@gentoo.org>  
  
# Lets just make sure we grab the latest quasselcore  
# with all the goodies  
RUN apt-get update && apt-get install -y quassel-core  
  
# Add our wrapper  
ADD wrap_quasselcore.sh /bin/  
  
# Create the configure directory. We do this here  
# because our container will be running as 'quasselcore' which  
# will not have the privs to do it itself.  
RUN mkdir -p /var/lib/quasselcore && chown -R quasselcore:quassel
/var/lib/quasselcore  
  
# Running USER  
USER quasselcore  
  
# Allow users to override the default port  
ENV QUASSEL_PORT=4242  
  
# Default params. Probably worth enforcing SSL  
# in ENTRYPOINT later on.  
  
CMD ["--configdir=/var/lib/quasselcore", "--require-ssl"]  
ENTRYPOINT ["wrap_quasselcore.sh"]  
  
# Expose the running port  
EXPOSE ${QUASSEL_PORT}  

