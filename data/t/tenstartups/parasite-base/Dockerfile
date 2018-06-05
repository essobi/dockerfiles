#  
# Parasite server initialization and configuration docker image base for
CoreOS  
#  
# http://github.com/tenstartups/parasite-docker  
#  
FROM tenstartups/alpine:latest  
  
LABEL maintainer="Marc Lennox <marc.lennox@gmail.com>"  
  
# Set environment  
ENV \  
PARASITE_OS=coreos \  
HOME=/home/parasite \  
RUBYLIB=/home/parasite/lib  
  
# Install base packages.  
RUN \  
apk --update add build-base figlet file-dev ruby-dev ruby-irb ruby-json && \  
rm -rf /var/cache/apk/*  
  
# Install gems.  
RUN gem install awesome_print net_http_unix ruby-filemagic --no-document  
  
# Set the working directory.  
WORKDIR "/home/parasite"  
  
# Copy source files and entrypoint.  
COPY lib lib  
COPY entrypoint.rb /docker-entrypoint  
  
# Copy parasite files.  
COPY conf.d conf.d  
# The directory name under parasite must match the name of the conf.d script  
COPY files 10-base  
  
# Set the entrypoint script.  
ENTRYPOINT ["/docker-entrypoint"]  
  
# Set the default command  
CMD ["/bin/bash"]  
  
# Dump the revision argument to file if present  
ONBUILD ARG BUILD_REVISION  
ONBUILD RUN echo ${BUILD_REVISION} > ./REVISION  

