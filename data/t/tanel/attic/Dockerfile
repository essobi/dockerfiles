FROM debian:wheezy-slim  
  
ENV VERSION 0.16  
RUN mkdir /code  
  
WORKDIR /code  
  
ADD https://attic-backup.org/downloads/releases/$VERSION/Attic-$VERSION-
linux-x86_64.tar.gz /code  
  
RUN tar xzf Attic-$VERSION-linux-x86_64.tar.gz && \  
mv Attic-$VERSION-linux-x86_64 attic  
  
# Dunno...  
ENV ATTIC_UNKNOWN_UNENCRYPTED_REPO_ACCESS_IS_OK=yes  
  
ENTRYPOINT ["/code/attic/attic"]  

