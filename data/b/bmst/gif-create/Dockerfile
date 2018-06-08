# Optimized by docker-optimize: https://www.npmjs.com/package/docker-optimize  
FROM ubuntu:16.04  
MAINTAINER Bogdan Mustiata <bogdan.mustiata@gmail.com>  
ENV { "UID":"1000","GID":"1000" }  
CMD perl -pi -e "s/raptor:x:1000:1000/raptor:x:$UID:$GID/" /etc/passwd && perl
-pi -e "s/raptor:x:1000:/raptor:x:$GID:/" /etc/group  
ADD bin/create-gif.py /usr/lib/gimp/2.0/plug-ins/create-gif.py  
RUN apt-get update -y && apt-get upgrade -y && useradd -m raptor && apt-get
install -y libav-tools gimp  
USER raptor  
ENV {
"INPUT_FILE":"/tmp/in/test.avi","OUTPUT_FILE":"/tmp/out/test.gif","WRITE_FOLDER":"/tmp/write","OUTPUT_FILE_NAME":"test.gif","SCALING_FACTOR":"1"
}  
ADD bin /home/raptor/bin  
CMD /home/raptor/bin/run_conversion.sh $OUTPUT_FILE_NAME $SCALING_FACTOR  

