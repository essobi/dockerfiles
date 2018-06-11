FROM haproxy  
  
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg  
  
RUN groupadd -r haproxy && useradd -r -g haproxy haproxy && touch
/run/haproxy.pid && chgrp haproxy /run/haproxy.pid && chmod g+w
/run/haproxy.pid  
USER haproxy  

