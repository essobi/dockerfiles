FROM ketkar/machine-learning-keras-cuda-gpu-tensorflow-opencv:latest  
  
# Copy pretrained weights  
RUN wget
https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5  
  
# Directory setup, file copying.  
COPY mrcnn/ ./mrcnn/  
COPY samples/ ./samples/  
  
# Logs dir is required by code.  
RUN mkdir logs/  
  

