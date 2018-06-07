# Header  
FROM ubuntu:latest  
  
ENV JELLYFISH_VERSION "2.2.6"  
# Update the package cache  
RUN apt-get update && apt-get install -y \  
build-essential \  
tar  
  
# Get and install Jellyfish  
# Note that the Python, Ruby, and Perl bindings are not enabled  
# To enable them: ./configure --enable-ruby-binding --enable-python-binding
--enable-perl-binding  
ADD
https://github.com/gmarcais/Jellyfish/releases/download/v$JELLYFISH_VERSION/jellyfish-$JELLYFISH_VERSION.tar.gz
\  
jellyfish.tar.gz  
RUN mkdir /src/ && \  
tar zxvf jellyfish.tar.gz -C /src/ --strip-components=1 && \  
cd /src/ && \  
./configure && \  
make && \  
make install  
  
# Add to system search paths  
ENV PATH="/src/bin/:$PATH" \  
LD_LIBRARY_PATH="/src/lib/:$LD_LIBRARY_PATH" \  
MANPATH="/src/share/man:$MANPATH" \  
PKG_CONFIG_PATH="/src/lib/pkgconfig:$PKG_CONFIG_PATH"  

