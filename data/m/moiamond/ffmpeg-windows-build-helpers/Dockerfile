FROM moiamond/ffmpeg-windows-build-helpers:crosstool-win  
MAINTAINER moiamond <moiamond@gmail.com>  
  
WORKDIR /build  
  
COPY ./cross_compile_ffmpeg.sh cross_compile_ffmpeg.sh  
  
CMD ["--help"]  
ENTRYPOINT ["./cross_compile_ffmpeg.sh"]

