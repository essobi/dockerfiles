FROM jjmerelo/alpine-perl6:latest  
LABEL version="3.0" maintainer="JJ Merelo <jjmerelo@GMail.com>"
perl6version="2018.04"  
  
# Set up dirs  
RUN mkdir /test  
VOLUME /test  
WORKDIR /test  
  
# Will run this  
ENTRYPOINT perl6 -v && zef install --deps-only . && zef test .  
  
# Repeating mother's env  
ENV PATH="/root/.rakudobrew/bin:${PATH}"  

