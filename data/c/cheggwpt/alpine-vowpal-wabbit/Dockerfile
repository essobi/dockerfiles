FROM alpine:3.6  
# Load ash profile on launch  
ENV ENV="/etc/profile"  
# ENV vars for project  
ENV VOWPAL_WABBIT_DATAFILE /app/model.vw  
ENV VOWPAL_WABBIT_PORT 4000  
  
# Setup ash profile prompt and my old man alias  
# Create work directory  
# since we're using virtual packages - allow cache so indexs are only fetched
once  
# Install dumb-init as a singleton  
# Install build tools as a virtual package  
# Install build dependencies as a virtual package  
# Git shallow clone of vowpal_wabbit master  
# build it and install  
# Clean up the container best we can  
# Install exec dependencies as a virtual package  
RUN mv /etc/profile.d/color_prompt /etc/profile.d/color_prompt.sh && \  
echo alias dir=\'ls -alh \--color\' >> /etc/profile && \  
mkdir -p /app && \  
apk \--update add dumb-init && \  
apk add \--virtual build-tools build-base git && \  
apk add \--virtual build-deps python3-dev boost-dev zlib-dev && \  
git clone \--depth 1 \--branch master \--single-branch \  
git://github.com/JohnLangford/vowpal_wabbit.git /app/build && \  
cd /app/build && make && make install &&\  
cd / && \  
apk del build-tools build-deps && \  
rm -rf /var/cache/apk/* && rm -rf /app/build && \  
apk \--no-cache add \--virtual run-deps boost-program_options zlib libstdc++  
  
# setup our working directory and copy over our codebase  
WORKDIR /app  
COPY ./data /app  
# set up dumb-init as the entry point  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
  
# generic command to start vowpal wabbit in daemon mode  
CMD vw -i ${VOWPAL_WABBIT_DATAFILE} \--port ${VOWPAL_WABBIT_PORT}
\--loss_function logistic \--link logistic \--daemon \--foreground  

