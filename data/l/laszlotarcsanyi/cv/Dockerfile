FROM alpine  
  
ENV BUILD_DEPS="git build-base"  
ENV DEPS="ncurses-dev"  
RUN apk update &&\  
apk add --no-cache $BUILD_DEPS $DEPS &&\  
git clone https://github.com/visit1985/mdp.git &&\  
cd mdp &&\  
make &&\  
make install &&\  
apk del $BUILD_DEPS  
  
COPY laszlo_tarcsanyi_cv.md cv.md  
  
ENTRYPOINT ["mdp","cv.md"]  

