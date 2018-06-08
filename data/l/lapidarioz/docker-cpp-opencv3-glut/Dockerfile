FROM kavolorn/opencv  
  
# Install OpenGL  
RUN apt-get -y install libxmu-dev libxi-dev freeglut3 freeglut3-dev  
  
RUN mkdir -p /usr/src/app  
RUN mkdir -p /usr/src/app-build  
WORKDIR /usr/src/app-build  
  
COPY CMakeLists.txt /usr/src/app/  
COPY main.cpp /usr/src/app/  
  
RUN cmake /usr/src/app/  
RUN cmake --build /usr/src/app-build --config Release  
  
RUN /usr/src/app-build/glut-container  

