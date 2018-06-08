FROM otakemaru/passenger-ruby22:5.0.28  
RUN apt-get update \  
&& apt-get install -y unzip \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN mkdir -p /usr/share/fonts \  
&& cd /usr/share/fonts \  
&& curl \  
\--location \  
\--silent \  
\--retry 3 \  
\--remote-name \  
"http://jaist.dl.sourceforge.jp/mix-mplus-ipa/63544/migmix-2p-20150712.zip" \  
&& unzip migmix-2p-20150712.zip \  
&& rm -f migmix-2p-20150712.zip \  
&& fc-cache -fv  
  

