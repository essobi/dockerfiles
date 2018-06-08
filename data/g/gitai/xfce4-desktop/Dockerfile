FROM alpine  
MAINTAINER Gitai<gitai.cn@gmail.com>  
LABEL maintainer "Gitai<gitai.cn@gmail.com>"  
  
RUN echo "@edge http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories && \  
echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
  
RUN apk update && \  
apk add curl jq && \  
apk add xfce4 paper-gtk-theme@testing paper-icon-theme@testing  
  
# RUN apk add lxappearance@testing  
ENV HOME /home/user  
COPY .gtkrc-2.0 $HOME/.gtkrc-2.0  
COPY xsettings.xml $HOME/.config/xfce4/xfconf/xfce-perchannel-
xml/xsettings.xml  
COPY xfwm4.xml $HOME/.config/xfce4/xfconf/xfce-perchannel-xml/xfwm4.xml  
RUN adduser -h $HOME -D user \  
&& chown -R user:user $HOME  
  
ENV PATH="/opt/lattice/bin:${PATH}"  
WORKDIR $HOME  
  
ENTRYPOINT [ "startxfce4" ]

