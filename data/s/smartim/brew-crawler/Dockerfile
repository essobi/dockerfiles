# SELECT IMAGE  
FROM debian:stretch  
  
# Install software  
RUN apt-get update; \  
apt-get install \  
apt-transport-https ca-certificates \  
build-essential gnupg gnupg2 wget curl git -y --no-install-recommends  
  
# Add Chrome Repo  
RUN curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add
- && \  
echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google-chrome.list  
  
## Install Chrome  
RUN apt-get update; apt-get install google-chrome-stable -y;  
  
# Add Chrome as a user  
RUN groupadd -r chrome && useradd -r -g chrome -G audio,video chrome \  
&& mkdir -p /home/chrome && chown -R chrome:chrome /home/chrome  
  
# Run Chrome non-privileged  
USER chrome  
  
  
  
# Expose port 9222  
EXPOSE 9222  
VOLUME /google  
WORKDIR /google  
  
# Autorun chrome headless with no GPU  
ENTRYPOINT [ "google-chrome-stable" ]  
CMD [ "--headless", "--disable-gpu", "--remote-debugging-address=0.0.0.0", "--
remote-debugging-port=9222", "${OPTS}" ]

