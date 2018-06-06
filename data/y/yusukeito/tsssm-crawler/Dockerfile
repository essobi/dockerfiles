FROM yusukeito/swift-basic:snapshot-2016-06-06-a  
  
#ENV APP_ENV dev  
ENV APP_TARGET RSSCrawler  
ENV APP_BUILD_ENV debug  
ENV APP_REPO tsssm-crawler  
  
# Clone & build our project  
COPY . /root/$APP_REPO  
RUN cd /root/$APP_REPO && \  
make $APP_BUILD_ENV && \  
mkdir /root/bin && \  
mv .build/$APP_BUILD_ENV/$APP_TARGET /root/bin/ && \  
rm -rf /root/$APP_TARGET  
  
# Launch  
CMD ["sh", "-c", "/root/bin/${APP_TARGET}"]  

