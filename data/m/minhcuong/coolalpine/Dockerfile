FROM alpine:latest  
  
LABEL maintainer="Trịnh Minh Cuong<cuong@techmaster.vn>"  
  
RUN apk update \  
&& apk add htop \  
vim \  
git \  
tree \  
curl \  
ncurses \  
util-linux \  
groff \  
bc \  
&& curl -O https://fishshell.com/files/2.7.0/fish-2.7.0.tar.gz \  
&& tar -zxvf fish-2.7.0.tar.gz \  
&& cd fish-2.7.0 \  
&& apk add --virtual build-deps \  
build-base \  
ncurses-dev \  
&& ./configure \  
&& make \  
&& make install \  
&& apk del build-deps \  
&& cd .. \  
&& rm -rf /fish-2.7.0 \  
&& rm /fish-2.7.0.tar.gz \  
&& rm -rf /var/cache/apk/* \  
&& curl -L https://get.oh-my.fish > ~/omf.fish \  
&& fish ~/omf.fish --noninteractive --path=~/.local/share/omf
--config=~/.config/omf \  
&& echo 'omf install budspencer;fish_update_completions;set -U
budspencer_nogreeting;rm ~/omf.fish;rm ~/.config/fish/config.fish' >
~/.config/fish/config.fish \  
&& fish  
COPY start.sh /  
COPY start.fish /  
  
ENTRYPOINT ["fish", "start.fish"]  

