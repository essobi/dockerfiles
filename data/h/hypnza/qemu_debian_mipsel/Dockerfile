FROM asmimproved/qemu-mips  
  
WORKDIR /root  
  
RUN apt-get update  
RUN apt-get install -y curl  
RUN curl -o vmlinux-3.2.0-4-4kc-malta
https://people.debian.org/~aurel32/qemu/mipsel/vmlinux-3.2.0-4-4kc-malta  
RUN curl -o debian_wheezy_mipsel_standard.qcow2
https://people.debian.org/~aurel32/qemu/mipsel/debian_wheezy_mipsel_standard.qcow2  
  
RUN mkdir /hostshare  
  
CMD qemu-system-mipsel -M malta -kernel vmlinux-3.2.0-4-4kc-malta -hda
debian_wheezy_mipsel_standard.qcow2 -append "root=/dev/sda1
console=ttyAMA0,115200" -nographic -fsdev
local,security_model=passthrough,id=fsdev0,path=/hostshare -device
virtio-9p-pci,id=fs0,fsdev=fsdev0,mount_tag=hostshare -serial mon:stdio  

