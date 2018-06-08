FROM debian:stretch  
  
# Install the build tools  
RUN apt-get update --assume-yes && \  
apt-get install -o 'Dpkg::Options::=--force-confnew' -y --force-yes -q gpg
wget build-essential && \  
apt-get autoclean  
  
# Build and Install, verifies the signature  
RUN mkdir /tmp/oathtool && cd /tmp/oathtool && \  
wget http://download.savannah.nongnu.org/releases/oath-toolkit/oath-
toolkit-2.6.2.tar.gz && \  
wget http://download.savannah.nongnu.org/releases/oath-toolkit/oath-
toolkit-2.6.2.tar.gz.sig && \  
gpg --keyserver hkp://pgp.mit.edu --recv-key 860B7FBB32F8119D && \  
gpg --verify oath-toolkit-2.6.2.tar.gz.sig oath-toolkit-2.6.2.tar.gz && \  
tar -x -f oath-toolkit-2.6.2.tar.gz && cd oath-toolkit-2.6.2 && \  
./configure --disable-shared --disable-pskc --disable-xmltest && \  
make && make check && make install && \  
cd ~/ && rm -rf /tmp/oathtool  
  
# Create a non root user to run the oath-tool as  
RUN useradd -ms /usr/bin/bash oath  
USER oath  
  
# Defaults to generating a TOTP token, provided that the user passes in the
secret  
ENTRYPOINT ["/usr/local/bin/oathtool", "--base32", "--totp"]  
  
LABEL com.opengov.maintainer=OpenGov \  
com.opengov.contact=devops@opengov.com \  
com.opengov.version=1.0.1  

