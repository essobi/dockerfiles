FROM shuieryin/erlang_ubuntu  
  
MAINTAINER Shuieryin <shuieryin@gmail.com>  
  
LABEL "version"="0.3.3" \  
"description"="Wechat mud game." \  
"author"="Shuieryin"  
  
WORKDIR /root/workspaces  
# checkout repos  
RUN git clone https://github.com/shuieryin/wechat_mud.git  
  
# build wechat_mud  
WORKDIR /root/workspaces/wechat_mud  
RUN git config --global user.email "shuieryin@gmail.com" \  
&& git config --global user.name "shuieryin" \  
&& make  
  
CMD make run

