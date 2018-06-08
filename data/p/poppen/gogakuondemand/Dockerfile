FROM jrottenberg/ffmpeg:3.3-alpine  
ENV GOGAKU_VER="1704_2"  
ADD https://www.dropbox.com/s/doysm8rod9aj588/gogaku${GOGAKU_VER}.zip?dl=1
/tmp  
WORKDIR /tmp  
RUN apk add --no-cache ruby && \  
apk add --no-cache --virtual .builddeps unzip && \  
unzip -x gogaku${GOGAKU_VER}.zip && \  
rm gogaku${GOGAKU_VER}.zip && \  
sed -i -E '/^def save_file_dest_dir/,/^end/s/\\./\/data/g'
gogaku${GOGAKU_VER}/pref.rb && \  
mv gogaku${GOGAKU_VER} /gogaku && \  
apk del .builddeps && \  
mkdir /data  
  
VOLUME /data  
ENTRYPOINT ["ruby", "/gogaku/gogakuondemand.rb"]  

