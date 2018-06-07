FROM shimjye/x2ubuntu  
LABEL maintainer="shimjye@gmail.com"  
  
RUN apt-get install -y fcitx fcitx-hangul locales  
RUN locale-gen ko_KR.UTF-8  
RUN mv /etc/localtime /etc/localtime.old  
RUN ln -s /usr/share/zoneinfo/Asia/Seoul /etc/localtime  
  
RUN /bin/cp /home/dockerx/dockerinit/kr/environment /etc/environment  
RUN /bin/cp /home/dockerx/dockerinit/kr/fcitx-autostart.desktop
/etc/xdg/autostart/fcitx-autostart.desktop  
RUN /bin/cp /home/dockerx/dockerinit/kr/profile /home/dockerx/.profile  
RUN chown 1000:1000 /home/dockerx/.profile  
  
RUN apt-get install -y wget curl vim git terminator  
  
EXPOSE 22  
CMD ["/run.sh"]  

