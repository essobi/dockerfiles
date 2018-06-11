# use the node base image provided by official repo  
FROM emitting/hexo  
MAINTAINER twiceYuan "twiceyuan@gmail.com"  
# prepare work directory  
VOLUME /root/.ssh  
  
ENV USER_NAME twiceYuan  
ENV USER_EMAIL twiceyuan@gmail.com  
  
RUN git config \--global user.name "$USE_NAME" && \  
git config \--global user.email "$USER_EMAIL"  

