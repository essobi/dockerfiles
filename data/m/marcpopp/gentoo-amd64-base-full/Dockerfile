FROM marcpopp/gentoo-amd64-base-full  
  
RUN emerge-webrsync && emerge --sync  
  
RUN source /etc/profile && \  
emerge --update --deep --newuse @world  
  

