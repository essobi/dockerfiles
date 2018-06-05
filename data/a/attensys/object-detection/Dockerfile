FROM victorhcm/opencv:3.2.0-python2.7  
WORKDIR /  
  
RUN git clone https://github.com/SebastianFlo/darknet darknet_build  
  
RUN cd darknet_build \  
&& git checkout basic-mvp \  
&& make OPENCV=1 \  
&& mv darknet .. \  
&& mv cfg ../cfg \  
&& mv data ../data  
  
RUN rm -rf /darknet_build  
  
# get weights  
RUN curl -O https://pjreddie.com/media/files/yolo.weights \  
&& curl -O https://pjreddie.com/media/files/tiny-yolo-voc.weights  
  
ENTRYPOINT []  
CMD ["/bin/bash"]  

