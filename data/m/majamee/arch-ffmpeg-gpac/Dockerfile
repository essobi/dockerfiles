FROM base/archlinux  
  
COPY ./transcode.sh /bin/transcode.sh  
  
RUN pacman -Sy --noconfirm && \  
pacman -S --noconfirm ffmpeg gpac git libxslt && \  
pacman -Scc --noconfirm && \  
git clone https://github.com/squidpickles/mpd-to-m3u8.git /app/mpd-to-m3u8 &&
\  
chmod +x /bin/transcode.sh  
  
COPY ./src /app/src  
  
WORKDIR /video  
ENTRYPOINT ["/bin/transcode.sh"]  
CMD ["*.mkv"]  

