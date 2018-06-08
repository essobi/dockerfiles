FROM selenium/standalone-chrome-debug:3.0.1-germanium  
RUN apt-get update && apt-get install -y ffmpeg gpac && rm -rf
/var/lib/apt/lists/*  
COPY scripts/ /scripts/  

