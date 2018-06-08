FROM julianbei/alpine-opencv-microimage:p2-3.1  
  
RUN apk add --update \  
libxml2-dev \  
libxslt-dev \  
libffi-dev \  
cairo \  
zip \  
freetype-dev \  
bash && \  
rm -rf /var/cache/apk/* && \  
pip install scipy==0.19.0 scikit-learn==0.18.1 scikit-image==0.13.0
unireedsolomon==1.0 svgwrite==1.1.10 svgutils==0.2.0 cairocffi==0.8.0
CairoSVG==1.0.22  
  
RUN mv /usr/local/lib/python2.7/site-packages/cv2.so /usr/lib/python2.7/site-
packages/cv2.so && \  
ln /dev/null /dev/raw1394  

