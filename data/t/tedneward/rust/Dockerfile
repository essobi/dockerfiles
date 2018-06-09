FROM rust  
MAINTAINER Ted Neward <ted@tedneward.com>  
  
RUN groupadd --gid 1000 rust \  
&& useradd --uid 1000 --gid rust --shell /bin/bash --create-home rust  
  
RUN chown -R rust:rust /usr/local  
  
USER rust  
WORKDIR /home/rust  
VOLUME ["/home/rust/work"]  
  
CMD ["/bin/bash"]

