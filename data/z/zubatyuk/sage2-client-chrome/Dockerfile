FROM zubatyuk/xorg-nvidia-352  
MAINTAINER Roman Zubatyuk <zubatyuk@gmail.com>  
  
ADD https://dl-ssl.google.com/linux/linux_signing_key.pub /root/  
RUN apt-key add /root/linux_signing_key.pub && rm /root/linux_signing_key.pub
\  
&& /bin/sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main"
>> /etc/apt/sources.list.d/google.list' \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \--no-install-recommends
\  
xdg-utils hicolor-icon-theme \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \--no-install-recommends
\  
google-chrome-stable libexif12 xdotool \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
RUN useradd -m -U chrome  

