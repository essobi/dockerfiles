FROM ubuntu:16.04  
LABEL version "1.1"  
LABEL description "Headless chromium builds."  
  
ENV APT_PACKAGES wget curl unzip apt-transport-https ca-certificates  
ENV CHROME_USER chrome  
ENV CHROMIUM_REVISION latest  
  
RUN mkdir -p /home/${CHROME_USER} && \  
groupadd --system ${CHROME_USER} && \  
useradd --system --gid ${CHROME_USER} ${CHROME_USER} && \  
chown -R ${CHROME_USER}:${CHROME_USER} /home/${CHROME_USER}  
  
ADD get_latest_chromium.sh /opt/get_latest_chromium.sh  
  
RUN apt-get update && \  
apt-get install --yes --no-install-recommends ${APT_PACKAGES} \  
$( apt-cache depends chromium-browser | awk '/\ Depends:/{print$2}' ) && \  
bash /opt/get_latest_chromium.sh && \  
apt-get remove --yes ${APT_PACKAGES} && \  
chown -R ${CHROME_USER}:${CHROME_USER} /opt/chrome-linux && \  
rm -rf /var/lib/apt/lists/*  
  
USER ${CHROME_USER}  
  
WORKDIR /opt/chrome-linux  
  
EXPOSE 9222  
ENTRYPOINT [ "./chrome", \  
"--headless", "--disable-gpu", \  
"--remote-debugging-address=0.0.0.0", \  
"--remote-debugging-port=9222" ]  

