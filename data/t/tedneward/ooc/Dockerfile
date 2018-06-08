FROM gcc  
MAINTAINER Ted Neward <ted@tedneward.com>  
  
# Build OOC to start with  
#  
RUN cd /usr/local && \  
git clone https://github.com/ooc-lang/rock.git && \  
cd rock && \  
make rescue  
ENV PATH=/usr/local/rock/bin:$PATH  
  
# All ooc-related "stuff" goes here  
RUN mkdir /home/ooc && \  
mkdir /home/ooc/Dev  
ENV OOC_LIBS=/home/ooc/Dev  
  
# Get sam in place  
#  
RUN git clone https://github.com/ooc-lang/sam.git ${OOC_LIBS}/sam && \  
cd ${OOC_LIBS}/sam && \  
rock -v  
  
WORKDIR /home/ooc  
  
ENTRYPOINT ["/bin/bash"]  

