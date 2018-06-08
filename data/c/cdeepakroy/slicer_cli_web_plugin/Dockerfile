FROM girder/slicer_cli_web  
MAINTAINER Deepak Roy Chittajallu <deepk.chittajallu@kitware.com>  
  
# Insert commands to install any system pre-requisites and libraries here  
# Copy files of the plugin into the docker container  
ENV SLICER_CLI_WEB_PLUGIN_PATH /opt/slicer_cli_web_plugin  
COPY . $SLICER_CLI_WEB_PLUGIN_PATH  
WORKDIR $SLICER_CLI_WEB_PLUGIN_PATH/Applications  
  
# pip install requirments.txt (if present) of each python CLI  
RUN find . -name requirements\\*.txt -print -exec pip install -U -r {} \;  
  
# Build C++ CLIs (Skip if you don't have C++ CLIs)  
RUN mkdir -p build && cd build && \  
echo "${PATH}" && \  
which cmake && \  
cmake \  
-G Ninja \  
-DCMAKE_BUILD_TYPE:STRING=Release \  
-DSlicerExecutionModel_DIR:PATH=$BUILD_PATH/SEM-build \  
../ && \  
ninja && \  
cd .. && \  
rm -rf build  
  
# use entrypoint of slicer_cli_web to expose slicer CLIS of this plugin on web  
ENTRYPOINT ["/build/miniconda/bin/python",
"/build/slicer_cli_web/server/cli_list_entrypoint.py"]  

