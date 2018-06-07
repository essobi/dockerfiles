FROM ubuntu:latest  
  
# Update  
RUN apt-get update -y  
  
ENV PACKAGES "libpq-dev"  
# Installing packages  
RUN apt-get install -y $PACKAGES  
  
# Cleanup  
RUN rm -rf $BUILD_DIR \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /usr/share/doc && rm -rf /usr/share/man \  
&& apt-get clean  

