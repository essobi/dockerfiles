# DOCKER-VERSION 0.3.4  
FROM ubuntu  
  
MAINTAINER Charles Nguyen <chuckleb@gmail.com>  
  
# Based off of instructions by Miguel Grinberg  
# http://blog.miguelgrinberg.com/post/how-to-build-and-run-mjpg-streamer-on-
the-raspberry-pi  
# Turn off intaractive mode to reduce noise and errors  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update path  
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
ENV LD_LIBRARY_PATH /usr/local/lib  
  
# Run updates and install base libs & tools  
RUN apt-get -y update  
RUN apt-get -y install build-essential wget unzip \  
libjpeg8-dev imagemagick libv4l-dev  
  
# MJPG-Streamer looks for videodev.h instead of videodev2.h  
RUN ln -s /usr/include/linux/videodev2.h /usr/include/linux/videodev.h  
  
RUN wget --no-check-certificate \  
http://sourceforge.net/code-snapshots/svn/m/mj/mjpg-streamer/code/mjpg-
streamer-code-182.zip && \  
unzip mjpg-streamer-code-182.zip && \  
cd mjpg-streamer-code-182/mjpg-streamer && \  
make mjpg_streamer input_file.so output_http.so output_file.so && \  
make install && \  
cd / ; rm -rf mjpg*  
  
VOLUME ["/data"]  
EXPOSE 8080  
RUN echo 'mjpg_streamer -i "input_file.so -f /data -n webcam.jpg" -o
"output_http.so -w /data/webroot"' > /start.sh && chmod a+rx /start.sh  
  
ENTRYPOINT /start.sh  

