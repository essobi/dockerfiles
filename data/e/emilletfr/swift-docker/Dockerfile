FROM emilletfr/ubuntu-docker:16.04  
MAINTAINER Eric Millet <emilletfr@gmail.com>  
  
ENV SWIFT_BRANCH swift-DEVELOPMENT-SNAPSHOT-2017-01-05-a  
ENV SWIFT_VERSION swift-DEVELOPMENT-SNAPSHOT-2017-01-05-a  
ENV SWIFT_PLATFORM ubuntu16.04  
# Install related packages and set LLVM 3.6 as the compiler  
RUN apt-get update && \  
apt-get install -y build-essential wget clang-3.6 curl libedit-dev python2.7
python2.7-dev libicu-dev rsync libxml2 git libcurl4-openssl-dev && \  
update-alternatives --install /usr/bin/clang clang /usr/bin/clang-3.6 100 && \  
update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-3.6
100 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install Swift keys  
RUN wget -q -O - https://swift.org/keys/all-keys.asc | gpg --import - && \  
gpg --keyserver hkp://pool.sks-keyservers.net --refresh-keys Swift  
  
# Install Swift Ubuntu 14.04 Snapshot  
RUN SWIFT_ARCHIVE_NAME=$SWIFT_VERSION-$SWIFT_PLATFORM && \  
SWIFT_URL=https://swift.org/builds/development/$(echo "$SWIFT_PLATFORM" | tr
-d .)/$SWIFT_VERSION/$SWIFT_ARCHIVE_NAME.tar.gz && \  
wget $SWIFT_URL && \  
wget $SWIFT_URL.sig && \  
gpg --verify $SWIFT_ARCHIVE_NAME.tar.gz.sig && \  
tar -xvzf $SWIFT_ARCHIVE_NAME.tar.gz --directory / --strip-components=1 && \  
rm -rf $SWIFT_ARCHIVE_NAME* /tmp/* /var/tmp/*  
  
# Set Swift Path  
ENV PATH /usr/bin:$PATH  
  
# Print Installed Swift Version  
RUN swift --version  
  
#RUN docker run -v /var/run/docker.sock:/var/run/docker.sock \  
# --privileged \  
# -p 8080:8080 -p 50000:50000 \  
# -v /Users/eric/Desktop/JenkinsBackup:/var/jenkins_home jenkins \  
# jenkins  
#/your/home:/var/jenkins_home jenkins  
#docker run -v /var/run/docker.sock:/var/run/docker.sock \  
# -v $(which docker):/usr/local/bin/docker \  
# -p 5000:5000 -p 8080:8080 \  
# -v /data/jenkins:/var/jenkins \  
# --privileged \  
# --restart always \  
# gianarb/jenkins:2.0  

