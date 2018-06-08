FROM ubuntu as build  
  
RUN apt-get update \  
&& apt-get install -y curl wget unzip  
  
RUN curl -L \  
"https://storage.googleapis.com/tensorflow/libtensorflow/libtensorflow-cpu-
linux-x86_64-1.7.0.tar.gz" | tar -C /usr/local -xz  
  
RUN wget https://github.com/tensorflow/tensorflow/archive/v1.7.0.zip \  
&& unzip v1.7.0.zip \  
&& mkdir tensorflow \  
&& mv tensorflow-1.7.0/tensorflow/go ./tensorflow \  
&& rm -rf tensorflow-1.7.0 v1.7.0.zip  
  
FROM golang:1.10.1  
  
COPY --from=build /usr/local/lib/libtensorflow*.so /usr/local/lib/  
COPY --from=build /usr/local/include/tensorflow /usr/local/include/tensorflow/  
  
ENV LD_LIBRARY_PATH /usr/local/lib  
ENV LIBRARY_PATH /usr/local/lib  
  
COPY --from=build /tensorflow/go
/go/src/github.com/tensorflow/tensorflow/tensorflow/go/  
  
ENV TF_CPP_MIN_LOG_LEVEL 2  
  
WORKDIR $GOPATH  

