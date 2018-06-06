FROM debian:jessie  
  
ADD https://raw.githubusercontent.com/ericfont/MuseScore/compile-
armhf/build/Linux%2BBSD/portable/RecipeDebian /  
ADD https://github.com/ericfont/docker-qt/releases/download/Qt-5.9.4-static-
jessie-armv7/Qt-5.9.4-static-debian-jessie-armv7.tar.gz /  
RUN chmod +x RecipeDebian  
RUN ./RecipeDebian --fetch-build-dependencies-only armhf  
RUN ./RecipeDebian --fetch-package-dependencies-only armhf  

