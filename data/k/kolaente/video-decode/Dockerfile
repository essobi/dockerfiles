FROM docker  
  
# Add bash, needed for our conversion script  
RUN apk add --update bash util-linux jq bc && rm -rf /var/cache/apk/*  
  
# Create folders  
RUN mkdir /var/videos && \  
mkdir -p /var/videoconversion/config  
  
# Add the actual script  
COPY convert.sh /var/videoconversion/  
COPY video_formats.json /var/videoconversion/config/  
  
RUN chmod +x /var/videoconversion/convert.sh  
  
# Volumes  
VOLUME /var/videos  
VOLUME /var/videoconversion/config  
  
ENV VIDEO_FOLDER=/var/videos  
  
CMD bash ./var/videoconversion/convert.sh -c
/var/videoconversion/config/video_formats.json -p /var/videos -f "docker run
-v $VIDEO_FOLDER:/var/videos jrottenberg/ffmpeg:3.4-alpine" -i "docker run -v
$VIDEO_FOLDER:/var/videos sjourdan/ffprobe"  

