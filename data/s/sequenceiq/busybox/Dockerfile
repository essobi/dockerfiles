FROM progrium/busybox  
  
RUN opkg-install bash unzip curl vim bind-tools  
RUN curl -o /usr/bin/jq http://stedolan.github.io/jq/download/linux64/jq \  
&& chmod +x /usr/bin/jq  
RUN curl -sLk j.mp/seq-bashrc|sed '0,/^USAGE/ d' > /root/.bashrc  
  
CMD bash  

