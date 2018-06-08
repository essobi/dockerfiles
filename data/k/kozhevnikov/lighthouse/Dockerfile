FROM node:8  
ENV CACHE 2017-08-23  
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key
add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google-chrome.list  
  
RUN apt-get update \  
&& apt-get install -y sudo xvfb google-chrome-stable \  
&& npm install -g lighthouse  
  
ENV USER lighthouse  
ENV HOME /home/$USER  
RUN groupadd -g 500 $USER \  
&& useradd -u 500 -g 500 -G root,sudo -m $USER \  
&& passwd -d $USER \  
&& echo "Defaults lecture=never" > /etc/sudoers.d/lecture  
  
USER $USER  
WORKDIR $HOME  
  
COPY *.sh ./  
ENV CHROME_PATH $HOME/chrome.sh  
RUN ln -s $HOME/docker.sh /usr/local/bin/docker  
  
ENTRYPOINT ["docker"]  
CMD ["lighthouse", "--help"]  

