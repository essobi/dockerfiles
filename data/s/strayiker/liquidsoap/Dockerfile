FROM ocaml/opam:debian-9_ocaml-4.05.0  
LABEL maintainer="Kirill Mesnyankin <sadbox.games@gmail.com>"  
  
ENV PACKAGES " \  
cry ao portaudio alsa pulseaudio bjack gstreamer \  
mad taglib lame shine ogg vorbis speex theora opus fdkaac faad flac \  
ladspa soundtouch samplerate \  
gavl ffmpeg frei0r \  
dssi \  
xmlplaylist lastfm lo \  
dtools duppy mm liquidsoap \  
"  
USER root  
  
# For libfdk-aac-dev  
RUN sed -e "s#main#main contrib non-free#" -i /etc/apt/sources.list  
  
RUN apt-get update  
  
USER opam  
  
RUN opam depext $PACKAGES && \  
opam pin add ffmpeg https://github.com/savonet/ocaml-
ffmpeg/releases/download/0.1.2/ocaml-ffmpeg-0.1.2.tar.gz && \  
opam install --verbose $PACKAGES  
  
ENTRYPOINT ["opam", "config", "exec", "--", "liquidsoap"]  
CMD ["-h"]  

