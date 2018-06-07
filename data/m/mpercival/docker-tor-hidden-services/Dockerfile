FROM patrickod/tor  
MAINTAINER Mark Percival <m@mdp.im>  
  
RUN useradd -ms /bin/bash toruser  
RUN mkdir -p /home/toruser/tor /home/toruser/tor/hidden_service  
VOLUME /root/hidden_service.key  
  
ADD ./torrc /home/toruser/torrc  
ADD ./start-tor /bin/start-tor  
  
CMD /bin/start-tor  

