FROM debian  
  
LABEL maintainer "Cornelius A. Ludmann <docker@cornelius-ludmann.de>"  
  
# Install SpiderOakONE  
# gnupg is required for the post install script of SpiderOakONE starting with
version 6.3.0 ('apt-key')  
RUN apt-get update && apt-get install -y \  
curl \  
gnupg \  
&& rm -rf /var/lib/apt/lists/*  
RUN curl -Ls -o spideroakone.deb
"https://spideroak.com/release/spideroak/deb_x64" && \  
dpkg -i spideroakone.deb && \  
rm -f spideroakone.deb  
  
# Create group and user  
ARG USER=spideroakone  
ARG GROUP=spideroakone  
ARG UID=1000  
ARG GID=1000  
RUN groupadd -fg ${GID} ${GROUP} && \  
useradd -r -g ${GID} -u ${UID} -s /bin/bash -d /spideroakone -m ${USER}  
  
# Create volumes  
RUN mkdir -p /spideroakone/.config/SpiderOakONE && \  
chown -R ${USER}:${GROUP} /spideroakone/.config && \  
mkdir /spideroakone/data && \  
chown ${USER}:${GROUP} /spideroakone/data  
VOLUME /spideroakone/.config/SpiderOakONE  
VOLUME /spideroakone/data  
  
# Change user and workdir  
USER ${USER}  
WORKDIR /spideroakone  
  
# Entrypoint  
#ENTRYPOINT ["/bin/bash"]  
ENTRYPOINT ["SpiderOakONE"]  
CMD ["--help"]  

