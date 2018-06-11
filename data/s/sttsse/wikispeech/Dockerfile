# Download sttsse/wikispeech_base from hub.docker.com | source repository:
https://github.com/stts-se/wikispeech_mockup: docker/wikispeech_base  
FROM sttsse/wikispeech_base  
  
LABEL "se.stts.vendor"="STTS - Speech technology services - http://stts.se"  
  
RUN mkdir -p /wikispeech/bin  
WORKDIR "/wikispeech"  
  
RUN git clone https://github.com/stts-se/wikispeech_mockup.git  
  
RUN mkdir -p /wikispeech/wikispeech_mockup/wikispeech_server/tmp  
RUN ln -s /wikispeech/wikispeech_mockup/docker/ws-postponed-start
/wikispeech/bin/  
  
# BUILD INFO  
ENV BUILD_INFO_FILE /wikispeech/.wikispeech_build_info.txt  
RUN echo "Application name: wikispeech" > $BUILD_INFO_FILE  
RUN echo -n "Build timestamp: " >> $BUILD_INFO_FILE  
RUN date --utc "+%Y-%m-%d %H:%M:%S %Z" >> $BUILD_INFO_FILE  
RUN echo "Built by: docker" >> $BUILD_INFO_FILE  
RUN echo -n "Git release: " >> $BUILD_INFO_FILE  
RUN cd /wikispeech/wikispeech_mockup && git describe --tags >>
$BUILD_INFO_FILE  
  
## RUNTIME SETTINGS  
EXPOSE 10000  
WORKDIR "/wikispeech/wikispeech_mockup"  
  
CMD python3 bin/wikispeech docker/config/docker.conf  
  

