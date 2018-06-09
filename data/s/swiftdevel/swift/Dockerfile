FROM swiftdevel/swiftdeps  
  
ENV SNAPSHOT_BRANCH development  
ENV SNAPSHOT_VERSION swift-DEVELOPMENT-SNAPSHOT-2017-08-21-a  
ENV SNAPSHOT_NAME ${SNAPSHOT_VERSION}-ubuntu16.04  
ENV SNAPSHOT_URL
https://swift.org/builds/${SNAPSHOT_BRANCH}/ubuntu1604/${SNAPSHOT_VERSION}/${SNAPSHOT_NAME}.tar.gz  
  
# Install tools  
RUN apt-get -y update \  
&& apt-get install -y wget vim nano curl wrk htop zsh  
  
# Temporary  
RUN apt-get install -y zlib1g-dev  
  
# Instal Oh my Zsh  
RUN bash -c "$(wget https://raw.github.com/robbyrussell/oh-my-
zsh/master/tools/install.sh -O -)" \  
&& sed -i -- 's/robbyrussell/simple/g' /root/.zshrc \  
&& sed -i -- 's/(git)/(git swiftpm)/g' /root/.zshrc  
  
# Git settings  
RUN git config --global credential.helper cache  
  
# Import the PGP keys  
RUN wget -q -O - https://swift.org/keys/all-keys.asc | gpg --import - \  
&& gpg --keyserver hkp://pool.sks-keyservers.net --refresh-keys Swift  
  
# Install Swift toolchain  
RUN wget ${SNAPSHOT_URL} && \  
wget ${SNAPSHOT_URL}.sig && \  
gpg --verify ${SNAPSHOT_NAME}.tar.gz.sig && \  
tar -xzf ${SNAPSHOT_NAME}.tar.gz && \  
rm ${SNAPSHOT_NAME}.tar.gz ${SNAPSHOT_NAME}.tar.gz.sig  
  
# Set Swift Path  
ENV PATH /${SNAPSHOT_NAME}/usr/bin:$PATH  
  
ENTRYPOINT zsh  

