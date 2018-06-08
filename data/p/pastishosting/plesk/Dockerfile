FROM plesk/plesk  
  
# Setup packages repositories  
RUN echo "deb http://fr.archive.ubuntu.com/ubuntu/ trusty multiverse" >
/etc/apt/sources.list.d/multiverse.list \  
&& echo "deb http://fr.archive.ubuntu.com/ubuntu/ trusty universe" >
/etc/apt/sources.list.d/universe.list  
  
# Install additional packages  
RUN apt-get update -y \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
openssh-server \  
postfix \  
rpl \  
rsync \  
rsyslog \  
software-properties-common \  
tmpreaper \  
vim \  
# Packages required by some legacy projects  
# -- radio.musiqueapproximative.net  
lame \  
libsox-fmt-mp3 \  
mp3gain \  
sox \  
# -- www.musiqueapproximative.net  
python-pip \  
python-pil \  
imagemagick \  
# incongru.org  
bc \  
# -- ouiedire.net,incongru.org  
eyeD3 \  
# mirror.pastis-hosting.net  
youtube-dl \  
# -- daheardit-records.net  
&& add-apt-repository ppa:heyarje/libav-11 \  
&& apt-get update -y \  
&& apt-get install -y \  
libav-tools \  
&& pip install \  
# -- www.musiqueapproximative.net  
bndr \  
&& rm -rf /var/lib/apt/lists/*  
  
# Configure packages  
RUN rpl "SHOWWARNING=true" "SHOWWARNING=false" /etc/tmpreaper.conf  
RUN locale-gen fr_FR.UTF-8  

