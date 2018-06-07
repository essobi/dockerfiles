FROM frolvlad/alpine-glibc:alpine-3.6  
ARG work_dir=/tmp/setup  
RUN mkdir ${work_dir} && \  
chmod 777 ${work_dir}  
  
# --- install roswell and some common lisp implementations --- #  
RUN apk add --no-cache --virtual=for-build git automake autoconf make gcc
build-base curl-dev glib-dev && \  
cd ${work_dir} && \  
git clone \--depth=1 -b release https://github.com/roswell/roswell.git && \  
cd roswell && \  
sh bootstrap && \  
./configure --disable-manual-install && \  
make && \  
make install && \  
cd .. && \  
rm -rf roswell && \  
apk del for-build  
  
RUN apk add --no-cache make curl-dev && \  
ros run -q  
  
RUN ln -s ${HOME}/.roswell/local-projects work  
ENV PATH /root/.roswell/bin:${PATH}  
  
RUN apk add --no-cache openssl-dev  

