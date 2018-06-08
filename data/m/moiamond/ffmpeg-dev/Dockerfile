FROM moiamond/ffmpeg-dev:windows-deps-win32  
LABEL maintainer="moiamond@gmail.com"  
  
WORKDIR /build  
  
COPY cross_compile_ffmpeg.sh .  
COPY patches ./patches/  
  
CMD ["--help"]  
ENTRYPOINT ["./cross_compile_ffmpeg.sh"]  

