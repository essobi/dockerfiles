FROM norionomura/swift:40  
LABEL maintainer "Norio Nomura <norio.nomura@gmail.com>"  
  
RUN apt-get update && apt-get install -y \  
libsqlite3-dev ruby-dev && \  
rm -r /var/lib/apt/lists/*  
  
ENV SOURCEKITTEN_REVISION="0.21.0"  
ENV JAZZY_VERSION=""  
# Install SourceKitten  
RUN git clone \--branch $SOURCEKITTEN_REVISION
https://github.com/jpsim/SourceKitten.git && \  
cd SourceKitten && \  
swift build --configuration release --static-swift-stdlib && \  
mv `swift build --configuration release --static-swift-stdlib --show-bin-
path`/sourcekitten /usr/bin && \  
cd .. && \  
rm -rf SourceKitten && \  
gem install bundler && \  
gem install jazzy --version "$JAZZY_VERSION"  
  
# Print Installed SourceKitten Version  
RUN sourcekitten version  

