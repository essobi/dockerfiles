FROM alpine:edge  
RUN apk -U add libvirt-daemon libvirt-qemu qemu qemu-x86_64 qemu-system-x86_64
openssh supervisor && \  
rm -rf /var/cache/apk/*  
COPY supervisor.conf /supervisor.conf  
CMD ["/usr/bin/supervisord", "-n", "-c", "/supervisor.conf"]  

