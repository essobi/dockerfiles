FROM zimovnov/coursera-aml-docker  
  
LABEL maintainer="Pavel Belevich <belevichp@gmail.com>"  
  
# RUN git clone https://github.com/hse-aml/intro-to-dl.git  
RUN pip install tensorflow  
  
WORKDIR intro-to-dl  
  
# RUN jupyter nbconvert --to python download_resources.ipynb && python3
download_resources.py  

