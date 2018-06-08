## Custom Dockerfile  
FROM consol/ubuntu-xfce-vnc  
ENV REFRESHED_AT 2018-04-12  
USER 0  
ARG VERSION=1.18  
ARG FILENAME=mendeleydesktop_${VERSION}-stable_amd64.deb  
ADD https://desktop-
download.mendeley.com/download/apt/pool/main/m/mendeleydesktop/${FILENAME} .  
  
RUN apt install ./"${FILENAME}"  
  
RUN rm "${FILENAME}"  
  
# Clean Up  
RUN apt-get clean && \  
apt-get autoremove --purge -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
## switch back to default user  
USER 1000  
RUN printf "\\\n\\\n# Startup Program\\\nmendeleydesktop &>
%s/mendeley_startup.log &" "$STARTUPDIR" >> "$HOME"/wm_startup.sh  

