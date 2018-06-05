FROM houselabs/s6  
MAINTAINER Chao Shen <shen218@gmail.com>  
ADD src /  
RUN echo https://mirrors.ustc.edu.cn/alpine/v3.4/main > /etc/apk/repositories
&& \  
echo https://mirrors.ustc.edu.cn/alpine/edge/community >>
/etc/apk/repositories  
  
RUN apk add --no-cache curl aria2 busybox bash\  
&& curl -L -s https://github.com/ziahamza/webui-aria2/archive/master.tar.gz \  
| tar xvzf - -C / \  
&& apk del --no-cache curl  
  
  
EXPOSE 6800 6801  
CMD ["/init"]  
  

