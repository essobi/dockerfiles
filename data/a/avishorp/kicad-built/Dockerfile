# Dockerfile for KiCAD  
FROM avishorp/kicad-deps  
  
# Checkout KiCAD  
RUN bzr whoami noone@nothing.com && bzr checkout lp:kicad /build/kicad.bzr  
  
# Run cmake for KiCAD  
RUN mkdir /build/kicad.bzr/build && cd /build/kicad.bzr/build && cmake ..  
  
# make KiCAD  
RUN make -j4 -C /build/kicad.bzr/build  
  
# Checkout the component library  
RUN bzr checkout lp:~kicad-product-committers/kicad/library /build/kicad-
library.bzr  
  
# Run cmake for component library  
RUN mkdir /build/kicad-library.bzr/build && cd /build/kicad-library.bzr/build
&& cmake ..  
  

