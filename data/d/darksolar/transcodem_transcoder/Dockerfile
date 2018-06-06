FROM darksolar/transcodem_base  
MAINTAINER suriya soutmun <suriya@tel.co.th>  
COPY entrypoint.sh /entrypoint.sh  
RUN curl -k https://codem-downloads.s3.amazonaws.com/codem-
transcoder_0.0.0_amd64.deb > /tmp/codem-transcoder_0.0.0_amd64.deb && \  
dpkg -i /tmp/codem-transcoder_0.0.0_amd64.deb && \  
rm -rf /tmp/* && \  
sed -i 's/\\(.*child_process.spawn.*\\)\\();\\)/\1, {cwd: outputDir}\2/'
/opt/codem-transcoder/codem-transcoder/lib/job.js && \  
echo "deb http://www.deb-multimedia.org jessie main non-free" >
/etc/apt/sources.list.d/multimedia.list && \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys 5C808C2B65558117 &&
\  
apt update && \  
apt install -y ffmpeg && \  
apt-get clean  
ENTRYPOINT [ "/entrypoint.sh" ]  
CMD [ "config/localhost_8080.json" ]  

