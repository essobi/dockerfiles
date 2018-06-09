FROM swift  
MAINTAINER Ted Neward <ted@tedneward.com>  
  
RUN groupadd --gid 1000 swift \  
&& useradd --uid 1000 --gid swift --shell /bin/bash --create-home swift  
  
USER swift  
WORKDIR /home/swift  
  
ENTRYPOINT ["/bin/bash"]

