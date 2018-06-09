FROM thenewvu/ubuntu-14.04  
MAINTAINER Vu Le "thenewvu@gmail.com"  
# download Google Chrome and install it  
RUN sudo wget --no-check-certificate
https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \  
{ sudo dpkg -i google-chrome-stable_current_amd64.deb || true; } && \  
sudo mkdir -p /usr/share/icons/hicolor && \  
sudo apt-get update && \  
sudo apt-get install -y --no-install-recommends -f  
  
# add the non-root user to group audio to enable sound  
RUN sudo usermod -aG audio vu  
  
# clean up  
RUN sudo rm google-chrome-stable_current_amd64.deb && \  
sudo apt-get clean && \  
sudo rm -rf /var/lib/apt/lists/*  
  
# start Google Chrome with a given user data directory  
ENTRYPOINT ["/usr/bin/google-chrome"]  
CMD ["--user-data-dir=/data"]  

