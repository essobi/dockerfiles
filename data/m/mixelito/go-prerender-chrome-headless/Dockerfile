FROM golang:1.8.3  
# Install deps + add Chrome Stable + purge all the things  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
ca-certificates \  
curl \  
gnupg \  
\--no-install-recommends \  
&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
\  
&& echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main"
> /etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update && apt-get install -y \  
google-chrome-beta \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
# Add Chrome as a user  
RUN groupadd -r chrome && useradd -r -g chrome -G audio,video chrome \  
&& mkdir -p /home/chrome && chown -R chrome:chrome /home/chrome  
  
# Run Chrome non-privileged  
USER chrome  
  
# Point to correct chrome location  
ENV CHROME_PATH /usr/bin/google-chrome-beta  
ENV PORT 9090  
EXPOSE 9090  
WORKDIR /go/src/app  
COPY . .  
  
RUN go-wrapper download  
RUN go-wrapper install  
  
CMD ["go-wrapper", "run"]  

