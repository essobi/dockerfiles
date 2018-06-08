FROM ubuntu:16.04  
LABEL name="chrome-headless"  
LABEL maintainer="btpka3 <btpka3@163.com>"  
LABEL version="0.1.0"  
LABEL description="Google Chrome Headless in a container"  
  
#RUN apt-get update  
#RUN apt-get install -y  
COPY linux_signing_key.pub /tmp  
  
RUN apt-key add /tmp/linux_signing_key.pub \  
&& rm /tmp/linux_signing_key.pub  
  
# install google chrome  
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main"
> /etc/apt/sources.list.d/google.list \  
&& apt-get update \  
&& apt-get install -y google-chrome-stable  
  
# install fonts :  
RUN apt-get install -y \  
fonts-horai-umefont \  
ttf-ubuntu-font-family \  
fonts-ubuntu-font-family-console \  
fonts-droid-fallback \  
fonts-roboto \  
xfonts-wqy \  
fonts-wqy-microhei \  
fonts-arphic-uming \  
fonts-unfonts-core \  
fonts-unfonts-extra \  
gsfonts \  
gsfonts-x11  
  
#RUN wget -O /tmp/ttf-mscorefonts-installer_3.6_all.deb
http://ftp.de.debian.org/debian/pool/contrib/m/msttcorefonts/ttf-mscorefonts-
installer_3.6_all.deb \  
# && dpkg -i /tmp/ttf-mscorefonts-installer_3.6_all.deb  
RUN rm -rf /var/lib/apt/lists/*  
  
# create not-root user  
RUN groupadd -r chrome \  
&& useradd -r -g chrome -G audio,video chrome \  
&& mkdir -p /home/chrome \  
&& chown -R chrome:chrome /home/chrome  
  
# Run Chrome non-privileged  
USER chrome  
  
#Expose port 9222  
EXPOSE 9222  
ENTRYPOINT [ "google-chrome-stable" ]  
CMD [ "--headless", "--disable-gpu", "--no-sandbox", "--remote-debugging-
address=0.0.0.0", "--remote-debugging-port=9222" ]

