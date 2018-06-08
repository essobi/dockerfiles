FROM perseids/dev-base  
# Add PPA: https://stackoverflow.com/questions/26217766/download-key-with-gpg-
recv-key-and-simultaneously-check-fingerprint-in-a-scr  
RUN echo "deb http://ppa.launchpad.net/hansjorg/rust/ubuntu trusty main" >>
/etc/apt/sources.list.d/rust.list && \  
echo "deb-src http://ppa.launchpad.net/hansjorg/rust/ubuntu trusty main" >>
/etc/apt/sources.list.d/rust.list && \  
bash -c 'set -e;tempName=$(mktemp);apt-key adv --status-fd 1 --keyserver
keyserver.ubuntu.com --recv-keys C03264CD6CADC10BFD6E708B37FD5E80BD6B6386 1>
$tempName 2>/dev/null;grep "^\\[GNUPG\:\\] IMPORT_OK [[:digit:]]*
C03264CD6CADC10BFD6E708B37FD5E80BD6B6386$" $tempName;grep "^\\[GNUPG\:\\]
IMPORT_RES 1" $tempName' && \  
apt-get update && apt-get -y install rust-nightly  
USER dev  
RUN git clone https://github.com/wting/rust.vim /home/dev/.vim  
WORKDIR /home/dev/project  
USER root  
RUN chown -R dev:dev /home/dev/  
CMD apt-get update && apt-get upgrade -y && su dev  

