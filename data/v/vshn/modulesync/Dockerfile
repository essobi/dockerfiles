FROM ruby:2.5.1  
LABEL maintainer "VSHN AG <tech@vshn.ch>"  
  
WORKDIR /app  
RUN git clone \--depth=1 https://github.com/voxpupuli/modulesync.git && \  
cd modulesync && \  
gem build modulesync.gemspec && \  
gem install --no-document modulesync-*.gem && \  
cd .. && \  
rm -rf modulesync  
  
CMD ["msync"]  

