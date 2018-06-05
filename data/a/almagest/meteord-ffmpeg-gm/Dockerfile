FROM abernix/meteord:node-4-base  
RUN apt-get update  
RUN apt-get install wget -y  
RUN apt-get install apt-utils -y  
RUN apt-get install graphicsmagick -y  
RUN apt-get install libdigest-hmac-perl -y  
RUN apt-get install libfile-copy-recursive-perl -y  
RUN apt-get install libio-tee-perl -y  
RUN apt-get install libunicode-string-perl -y  
RUN apt-get install libmail-imapclient-perl -y  
RUN apt-get install libterm-readkey-perl -y  
RUN apt-get install makepasswd rcs perl-doc libio-tee-perl git libmail-
imapclient-perl libdigest-md5-file-perl libterm-readkey-perl libfile-copy-
recursive-perl build-essential make automake libunicode-string-perl -y  
RUN apt-get install makepasswd libauthen-ntlm-perl libcrypt-ssleay-perl
libdigest-hmac-perl libfile-copy-recursive-perl libio-compress-perl libio-
socket-inet6-perl libio-socket-ssl-perl libio-tee-perl libmodule-scandeps-perl
libnet-ssleay-perl libpar-packer-perl libreadonly-perl libterm-readkey-perl
libtest-pod-perl libtest-simple-perl libunicode-string-perl liburi-perl
cpanminus -y  
  
RUN wget
https://gist.githubusercontent.com/lanmower/38e6175febd8b9a567cc9755ce7221db/raw/ad869f2abf0e56e0c83a3b7595e583de3d04f131/ffdshow.sh
-O /tmp/ffmpeg.sh  
RUN chmod +x /tmp/ffmpeg.sh  
RUN /tmp/ffmpeg.sh  
VOLUME ["/store/cfs"]  

