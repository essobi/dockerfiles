FROM siomiz/node-opencv  
  
RUN apt-get install -y vim amqp-tools telnet  
  
# https://github.com/mhart/alpine-node/issues/26  
RUN npm install fs-extra \  
&& cp -r node_modules/* /usr/local/lib/node_modules/npm/node_modules \  
&& sed -i s/graceful-fs/fs-extra/g
/usr/local/lib/node_modules/npm/lib/utils/rename.js \  
&& sed -i s/fs.rename/fs.move/g
/usr/local/lib/node_modules/npm/lib/utils/rename.js \  
&& rm -rf node_modules \  
&& npm install -g npm@latest  
  
RUN npm install amqp-ts opencv npm node-uuid underscore bloomrun  
  
RUN useradd -ms /bin/bash node  
USER node  
WORKDIR /home/node/projects/opencv/detector  
  
ADD js js  
  
# RabbitMQ settings  
ENV RABBITMQ_HOST=amqp://rabbitmq:5672  
ENV RABBITMQ_EXCHANGE_TYPE=fanout  
  
# Exchange and queue to insert faces  
ENV RABBITMQ_EXCHANGE_IMAGES=images  
ENV RABBITMQ_QUEUE_IMAGES=opencv.images  
  
# Exchange and queue for detected faces  
ENV RABBITMQ_EXCHANGE_FACES=faces  
ENV RABBITMQ_QUEUE_FACES=opencv.faces  
  
# Exchange and queue for outline of detected faces  
ENV RABBITMQ_EXCHANGE_FACES_OUTLINED=faces.outlined  
ENV RABBITMQ_QUEUE_FACES_OUTLINED=opencv.faces.outlined  
  
CMD node js/detector_opencv_faces.js  

