FROM ubuntu:17.10  
  
##############################################  
# configuration  
##############################################  
ENV CLAWS_VERSION 3.16.0  
ENV CLAWS_THEMES_VERSION 20140629  
ENV CLAWSKER_VERSION 1.1.0  
  
ENV USERNAME user  
ENV UID 1000  
ENV GID 1000  
##############################################  
# end configuration, dont touch below  
##############################################  
  
ENV CLAWS_REPO git://git.claws-mail.org/claws.git  
ENV CLAWS_THEMES_REPO git://git.claws-mail.org/themes.git  
ENV CLAWSKER_REPO http://git.claws-mail.org/readonly/clawsker.git  
  
RUN \  
apt-get update && \  
apt-get install --no-install-recommends -y \  
build-essential \  
git \  
bison \  
flex \  
automake \  
gettext \  
libtool \  
gettext \  
pkg-config \  
libglib2.0-dev \  
libgtk2.0-dev \  
libetpan-dev \  
libgpgme11-dev \  
libgtk2.0-dev \  
libwebkitgtk-dev \  
libpoppler-dev \  
libpoppler-glib-dev \  
libical-dev && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
git clone --branch ${CLAWS_VERSION} ${CLAWS_REPO} claws && \  
cd claws && ./autogen.sh && make -j $(nproc --all) && make install && \  
cd .. && rm -rf claws  
  
RUN git clone --branch ${CLAWS_THEMES_VERSION} ${CLAWS_THEMES_REPO}
clawsthemes && \  
cd clawsthemes && ./autogen.sh && make -j $(nproc --all) && make install && \  
cd .. && rm -rf clawsthemes  
  
RUN git clone --branch ${CLAWSKER_VERSION} ${CLAWSKER_REPO} clawswer && \  
cd clawswer && make install && \  
cd .. && rm -rf clawswer  
  
RUN \  
apt-get update && \  
apt-get install -y \  
pinentry-gtk2 \  
aspell-es \  
greybird-gtk-theme && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
groupadd --gid ${GID} ${USERNAME} && \  
useradd --uid ${UID} --gid ${GID} --create-home ${USERNAME}  
  
USER ${USERNAME}  
WORKDIR /home/${USERNAME}  
VOLUME /home/${USERNAME}  
  
CMD ["/usr/local/bin/claws-mail"]  

