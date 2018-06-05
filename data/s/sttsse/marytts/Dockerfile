# Download sttsse/wikispeech_base from hub.docker.com | source repository:
https://github.com/stts-se/wikispeech_mockup: docker/wikispeech_base  
FROM sttsse/wikispeech_base  
  
LABEL "se.stts.vendor"="STTS - Speech technology services - http://stts.se"  
  
RUN mkdir -p /wikispeech/bin  
WORKDIR "/wikispeech"  
  
##################### INSTALL MARYTTS #####################  
RUN git clone https://github.com/stts-se/marytts.git  
  
WORKDIR "/wikispeech/marytts"  
  
RUN ./gradlew installDist  
  
## INSTALL STTS VOICES  
RUN cp stts_voices/voice-ar-nah-hsmm-5.2.jar build/install/marytts/lib/  
RUN cp stts_voices/voice-dfki-spike-hsmm-5.1.jar build/install/marytts/lib/  
RUN cp stts_voices/voice-stts_no_nst-hsmm-5.2.jar build/install/marytts/lib/  
RUN cp stts_voices/voice-stts_sv_nst-hsmm-5.2-SNAPSHOT.jar
build/install/marytts/lib/  
  
## SCRIPT FOR LISTING VOICES  
RUN echo "echo 'AVAILABLE VOICES:' && ls
/wikispeech/marytts/build/install/marytts/lib/ | egrep ^voice | sed 's/.jar//'
| sed 's/^/* /' " > /wikispeech/bin/voices  
RUN chmod +x /wikispeech/bin/voices  
  
##################### INSTALL MISHKAL #####################  
WORKDIR "/wikispeech"  
  
# RUN git clone https://github.com/linuxscout/mishkal.git  
RUN git clone https://github.com/HaraldBerthelsen/mishkal.git  
  
WORKDIR "/wikispeech/mishkal"  
  
# NO LONGER NEEDED (FIXED IN HB'S VERSION):  
# RUN sed 's/self.display(word, format_display)/self.display(voc_word,
format_display)/' mishkal/tashkeel/tashkeel.py >
mishkal/tashkeel/tashkeel.py_UPDATE  
# RUN mv mishkal/tashkeel/tashkeel.py mishkal/tashkeel/tashkeel.py_OLD  
# RUN cp mishkal/tashkeel/tashkeel.py_UPDATE mishkal/tashkeel/tashkeel.py  
RUN echo "python /wikispeech/mishkal/interfaces/web/mishkal-webserver.py &" >
/wikispeech/bin/marytts-mishkal-start  
RUN echo "sleep 2" >> /bin/marytts-mishkal-start  
RUN echo "cd /wikispeech/marytts && ./gradlew run" >> /wikispeech/bin/marytts-
mishkal-start  
  
RUN chmod +x /wikispeech/bin/marytts-mishkal-start  
  
##################### AFTER INSTALL #####################  
WORKDIR "/wikispeech"  
  
# BUILD INFO  
ENV BUILD_INFO_FILE /wikispeech/.marytts_build_info.txt  
RUN echo "Application name: marytts" >> $BUILD_INFO_FILE  
RUN echo -n "Build timestamp: " >> $BUILD_INFO_FILE  
RUN date --utc "+%Y-%m-%d %H:%M:%S %Z" >> $BUILD_INFO_FILE  
RUN echo "Built by: docker" >> $BUILD_INFO_FILE  
RUN echo -n "Git release: " >> $BUILD_INFO_FILE  
RUN cd /wikispeech/marytts && git describe --tags >> $BUILD_INFO_FILE  
  
## LIST MARYTTS VOICES  
RUN /wikispeech/bin/voices  
  
## RUNTIME SETTINGS  
EXPOSE 59125  
CMD /wikispeech/bin/marytts-mishkal-start  
  

