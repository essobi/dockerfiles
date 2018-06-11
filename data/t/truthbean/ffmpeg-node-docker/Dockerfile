FROM debian  
  
ENV TZ=Asia/Shanghai  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
COPY sources.list /etc/apt/sources.list  
  
#RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list  
RUN apt-get update -y && apt-get dist-upgrade -y  
  
RUN apt-get install curl software-properties-common gnupg locales -y  
  
RUN locale-gen zh_CN.UTF-8 && DEBIAN_FRONTEND=noninteractive dpkg-reconfigure
locales  
RUN locale-gen zh_CN.UTF-8  
ENV LANG=zh_CN.UTF-8  
ENV LANGUAGE=zh_CN:zh  
RUN export LC_ALL=zh_CN.UTF-8  
  
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -  
  
RUN apt-get update -y  
  
RUN apt-get install -y ffmpeg nodejs python make g++  
  
RUN npm install yarn -g  
  
RUN yarn global add increase-memory-limit  
  
RUN yarn config set registry https://registry.npm.taobao.org -g  
  
CMD ["node"]

