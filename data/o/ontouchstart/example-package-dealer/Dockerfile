FROM ontouchstart/swift3:swift-3.0-PREVIEW-2  
ADD . example-package-dealer  
RUN cd example-package-dealer && swift build  
RUN example-package-dealer/.build/debug/Dealer  

