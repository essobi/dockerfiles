FROM luhmer/opencv-python3  
  
#WORKDIR /app/  
#RUN mkdir -p app/ml_models \  
# && cd app/ml_models \  
# && wget https://github.com/davisking/dlib-
models/raw/master/dlib_face_recognition_resnet_model_v1.dat.bz2 \  
# && wget https://github.com/davisking/dlib-
models/raw/master/shape_predictor_68_face_landmarks.dat.bz2 \  
# && bunzip2 dlib_face_recognition_resnet_model_v1.dat.bz2 \  
# && bunzip2 shape_predictor_68_face_landmarks.dat.bz2  
# #&& rm dlib_face_recognition_resnet_model_v1.dat.bz2 \  
# #&& rm shape_predictor_68_face_landmarks.dat.bz2  
RUN apt-get update \  
&& apt-get install -y git tzdata netcat \  
&& rm -rf /var/lib/apt/lists/*  
  
# matplotlib config (used by benchmark)  
RUN mkdir -p /root/.config/matplotlib \  
&& echo "backend : Agg" > /root/.config/matplotlib/matplotlibrc  
  
# copy the requirements file over  
COPY ./requirements.txt requirements.txt  
RUN pip3 install -U -r requirements.txt \  
&& rm requirements.txt  
  
WORKDIR /app/  
COPY . /app/  
  
CMD /bin/bash -c "sh ./wait-for mqtt-broker:1883 -t 60 -- sh startDocker.sh"  
#CMD /bin/bash -c "sh startDocker.sh"

