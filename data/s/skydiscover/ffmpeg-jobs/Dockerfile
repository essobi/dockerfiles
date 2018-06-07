FROM jrottenberg/ffmpeg:latest  
  
WORKDIR /  
  
ENV DISPLAY_REFRESH_RATE=5 \  
DISPLAY_MIN_DELTA=0 \  
PULL_REFRESH_RATE=5  
RUN apt-get update && apt-get install -y mediainfo python3 python3-pip && \  
pip3 install tqdm pexpect  
  
VOLUME /jobs  
COPY "./ffmpeg-jobs.py" "/ffmpeg-jobs.py"  
ENTRYPOINT python3 -u /ffmpeg-jobs.py --pull-refresh-rate $PULL_REFRESH_RATE
\--display-refresh-rate $DISPLAY_REFRESH_RATE  

