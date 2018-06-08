FROM quarry/node  
echo 'bump' /tmp/bumpversion  
RUN (mkdir /tmp/mon && cd /tmp/mon && curl -L#
https://github.com/visionmedia/mon/archive/master.tar.gz | tar zx --strip 1 &&
make install)  
RUN npm install component browserify -g

