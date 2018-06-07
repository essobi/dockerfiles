FROM nginx:latest  
  
MAINTAINER Eli Daian "elidaian@gmail.com"  
# Add static website content  
RUN mkdir -p /var/edsudoku/static /var/edsudoku/fonts  
  
# Add static bootstrap contents  
ADD
https://raw.githubusercontent.com/elidaian/sudoku/master/src/edsudoku/server/static/bootstrap-
theme.min.css \  
https://raw.githubusercontent.com/elidaian/sudoku/master/src/edsudoku/server/static/bootstrap.min.css
\  
https://raw.githubusercontent.com/elidaian/sudoku/master/src/edsudoku/server/static/bootstrap.min.js
\  
/var/edsudoku/static/  
ADD
https://github.com/elidaian/sudoku/raw/master/src/edsudoku/server/fonts/glyphicons-
halflings-regular.eot \  
https://github.com/elidaian/sudoku/raw/master/src/edsudoku/server/fonts/glyphicons-
halflings-regular.svg \  
https://github.com/elidaian/sudoku/raw/master/src/edsudoku/server/fonts/glyphicons-
halflings-regular.ttf \  
https://github.com/elidaian/sudoku/raw/master/src/edsudoku/server/fonts/glyphicons-
halflings-regular.woff \  
https://github.com/elidaian/sudoku/raw/master/src/edsudoku/server/fonts/glyphicons-
halflings-regular.woff2 \  
/var/edsudoku/fonts/  
  
# Add static jQuery contents  
ADD http://code.jquery.com/jquery-2.1.4.min.js /var/edsudoku/static/  
  
# Add custom static contents  
ADD
https://raw.githubusercontent.com/elidaian/sudoku/master/src/edsudoku/server/static/board.css
\  
https://raw.githubusercontent.com/elidaian/sudoku/master/src/edsudoku/server/static/customization.css
\  
/var/edsudoku/static/  
  
# Add nginx configuration  
COPY nginx.conf /etc/nginx/nginx.conf  
  

