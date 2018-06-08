FROM debian:stable  
  
RUN apt-get update && apt-get install -y wget  
  
# Download Sophos  
#RUN wget http://downloads.sophos.com/inst/mVmFIiepyqqvUm9Mo2q8SAZD00ODQ0/sav-
linux-free-9.tgz -O /tmp/sophos.tgz -q --show-progress --progress=dot:giga &&
\  
# cd /tmp && tar -xzvf /tmp/sophos.tgz  
# Unattended install Sophos AV Free, automatically answer the questions  
#RUN printf '\nN\n\nf\n\n' | /tmp/sophos-av/install.sh --acceptlicence
--autostart=False  
# Expose our CID first  
#VOLUME [ "/opt/sophos-av/update/cache/Primary" ]  
COPY ./savinstpkg.deb /  
RUN dpkg -i /savinstpkg.deb || true  
  
COPY ./entrypoint.sh /  
# Update, then run.  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["savscan", "-h"]  

