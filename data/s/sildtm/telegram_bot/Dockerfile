FROM sildtm/cpp_build:latest  
ENV PROJECT_NAME telegram_bot  
ENV PROJECT_ROOT_DIR /opt/${PROJECT_NAME}  
RUN \  
mkdir /opt && cd /opt && \  
git clone https://github.com/Sild/${PROJECT_NAME} && \  
cd ${PROJECT_ROOT_DIR} && \  
git submodule update --init --recursive  
  
WORKDIR ${PROJECT_ROOT_DIR}  
  
#RUN mkdir build && cd build && cmake ../ && cmake --build .  
RUN cmake . && cmake --build . && mkdir runnable_dir  
WORKDIR ${PROJECT_ROOT_DIR}/runnable_dir§  
  
CMD ["../assistant"]  

