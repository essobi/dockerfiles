FROM alpine:3.7  
RUN apk add --no-cache build-base freeglut-dev glew-dev mesa-demos cmake musl-
dev git xclock mesa-dri-intel  
  
#RUN mkdir /home/git; \  
# cd /home/git; \  
# sudo git clone https://github.com/DavidArayan/assimp.git -b master; \  
# cd assimp; \  
# mkdir build; \  
# cd build; \  
# cmake CMakeLists.txt -G 'Unix Makefiles' ../; \  
# make  
#RUN gcc -dM -E - < nul  
RUN mkdir /home/git; \  
cd /home/git; \  
git clone https://github.com/assimp/assimp.git -b master;  
  
RUN cd /home/git/assimp; \  
cmake CMakeLists.txt -G 'Unix Makefiles'; \  
make; \  
make install;  
#ldconfig;  
RUN assimp help  
CMD rm -rf /home/out/* && mv /home/git/assimp/bin /home/out/bin && mv
/home/git/assimp/lib /home/out/lib  

