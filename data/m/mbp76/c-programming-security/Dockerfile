FROM mbp76/docker-gradle  
MAINTAINER mbp76@users.noreply.github.com  
  
ADD . /home/builder  
WORKDIR /home/builder  
  
# Install gcc toolchain before the first build.  
RUN gradle dependencies  
CMD gradle --continuous  

