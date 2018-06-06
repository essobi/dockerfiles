# use Caffe2 image as parent image  
FROM caffe2/caffe2:snapshot-py2-cuda9.0-cudnn7-ubuntu16.04  
# addtional libraries: ffmpeg, sk-video (pip)  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ffmpeg wget vim  
  
RUN mv /usr/local/caffe2 /usr/local/caffe2_build  
ENV Caffe2_DIR /usr/local/caffe2_build  
  
ENV PYTHONPATH /usr/local/caffe2_build:${PYTHONPATH}  
ENV LD_LIBRARY_PATH /usr/local/caffe2_build/lib:${LD_LIBRARY_PATH}  
  
# Install Python dependencies  
RUN pip install numpy>=1.13 pyyaml>=3.12 matplotlib opencv-python>=3.2
setuptools Cython mock scipy sk-video  
  
# Install the COCO API  
RUN git clone https://github.com/cocodataset/cocoapi.git /cocoapi  
WORKDIR /cocoapi/PythonAPI  
RUN make install  
  
# Clone the Detectron repository  
RUN git clone https://github.com/suhangpro/detectron /detectron  
  
# Set up Python modules  
WORKDIR /detectron/lib  
RUN make  
  
# Build custom ops  
RUN make ops  
  
# entrypoint  
WORKDIR /detectron  
ENTRYPOINT ["python", "tools/infer_simple_img.py"]  
CMD ["demo"]  

