FROM fedora:23  
MAINTAINER Tomas Tomecek <ttomecek@redhat.com>  
ADD install_chromium.sh /  
RUN chmod +x install_chromium.sh && /install_chromium.sh  
  
LABEL Name="chromium" \  
Version="0.0.1" \  
Release="1"  
# change if your user ID is different  
ARG USER_ID=1000  
RUN useradd -o -u ${USER_ID} -G video chromium  
USER chromium  
ENV HOME=/home/chromium  
# --no-sandbox -- can run the container in an unprivileged mode  
CMD ["/usr/bin/chromium-browser", "--no-sandbox"]  

