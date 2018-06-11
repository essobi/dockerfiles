FROM ubuntu:16.04  
LABEL version "1.0"  
LABEL description "Headless unstable Google chrome."  
  
ENV APT_PACKAGES apt-transport-https curl  
ENV CHROME_USER chrome  
  
RUN mkdir -p /home/${CHROME_USER} && \  
groupadd --system ${CHROME_USER} && \  
useradd --system --gid ${CHROME_USER} ${CHROME_USER} && \  
chown -R ${CHROME_USER}:${CHROME_USER} /home/${CHROME_USER}  
  
RUN apt-get update && \  
apt-get install --yes ${APT_PACKAGES} && \  
curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - &&
\  
echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google-chrome-unstable.list && \  
apt-get update && \  
apt-get install --yes --no-install-recommends google-chrome-unstable && \  
rm -rf /var/lib/apt/lists/*  
  
USER ${CHROME_USER}  
  
WORKDIR /home/${CHROME_USER}  
  
EXPOSE 9222  
ENTRYPOINT [ "google-chrome-unstable", \  
"--headless", "--disable-gpu", \  
"--remote-debugging-address=0.0.0.0", \  
"--remote-debugging-port=9222" ]  

