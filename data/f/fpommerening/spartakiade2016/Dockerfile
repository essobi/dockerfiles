FROM base/arch  
MAINTAINER Frank Pommerening "frank@pommerening-online.de"  
ENV REFRESHED_AT 2016-02-15  
RUN useradd -u 1000 spartakiade  
RUN mkdir /projects  
RUN chown -R spartakiade:spartakiade /projects  
VOLUME ["/projects"]  
ENTRYPOINT ["/bin/bash"]  

