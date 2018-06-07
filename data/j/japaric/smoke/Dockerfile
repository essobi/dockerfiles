FROM ubuntu:16.04  
  
COPY setup.sh /  
RUN bash /setup.sh  
  
ENV \  
AR_aarch64_unknown_linux_gnu=aarch64-linux-gnu-ar \  
CARGO_TARGET_AARCH64_UNKNOWN_LINUX_GNU_LINKER=aarch64-linux-gnu-gcc \  
CC_aarch64_unknown_linux_gnu=aarch64-linux-gnu-gcc \  
CXX_aarch64_unknown_linux_gnu=aarch64-linux-gnu-g++ \  
\  
AR_arm_unknown_linux_gnueabi=arm-linux-gnueabi-ar \  
CARGO_TARGET_ARM_UNKNOWN_LINUX_GNUEABI_LINKER=arm-linux-gnueabi-gcc \  
CC_arm_unknown_linux_gnueabi=arm-linux-gnueabi-gcc \  
CXX_arm_unknown_linux_gnueabi=arm-linux-gnueabi-g++ \  
\  
AR_arm_unknown_linux_gnueabihf=arm-linux-gnueabi-ar \  
CARGO_TARGET_ARM_UNKNOWN_LINUX_GNUEABIHF_LINKER=arm-linux-gnueabihf-gcc \  
CC_arm_unknown_linux_gnueabihf=arm-linux-gnueabihf-gcc \  
CXX_arm_unknown_linux_gnueabihf=arm-linux-gnueabihf-g++ \  
\  
AR_armv7_unknown_linux_gnueabihf=arm-linux-gnueabi-ar \  
CARGO_TARGET_ARMV7_UNKNOWN_LINUX_GNUEABIHF_LINKER=arm-linux-gnueabihf-gcc \  
CC_armv7_unknown_linux_gnueabihf=arm-linux-gnueabihf-gcc \  
CXX_armv7_unknown_linux_gnueabihf=arm-linux-gnueabihf-g++ \  
\  
CARGO_TARGET_I686_UNKNOWN_LINUX_MUSL_LINKER=/musl/i686-unknown-linux-
musl/bin/musl-gcc \  
CC_i686_unknown_linux_musl=/musl/i686-unknown-linux-musl/bin/musl-gcc \  
CXX_i686_unknown_linux_musl=false \  
\  
AR_mips_unknown_linux_gnu=mips-linux-gnu-ar \  
CARGO_TARGET_MIPS_UNKNOWN_LINUX_GNU_LINKER=mips-linux-gnu-gcc \  
CC_mips_unknown_linux_gnu=mips-linux-gnu-gcc \  
CXX_mips_unknown_linux_gnu=mips-linux-gnu-g++ \  
\  
AR_mips_unknown_linux_musl=mips-openwrt-linux-ar \  
CARGO_TARGET_MIPS_UNKNOWN_LINUX_MUSL_LINKER=mips-openwrt-linux-gcc \  
CC_mips_unknown_linux_musl=mips-openwrt-linux-gcc \  
CXX_mips_unknown_linux_musl=mips-openwrt-linux-g++ \  
\  
AR_mipsel_unknown_linux_musl=mipsel-openwrt-linux-ar \  
CARGO_TARGET_MIPSEL_UNKNOWN_LINUX_MUSL_LINKER=mipsel-openwrt-linux-gcc \  
CC_mipsel_unknown_linux_musl=mipsel-openwrt-linux-gcc \  
CXX_mipsel_unknown_linux_musl=mipsel-openwrt-linux-g++ \  
\  
AR_mipsel_unknown_linux_gnu=mipsel-linux-gnu-ar \  
CARGO_TARGET_MIPSEL_UNKNOWN_LINUX_GNU_LINKER=mipsel-linux-gnu-gcc \  
CC_mipsel_unknown_linux_gnu=mipsel-linux-gnu-gcc \  
CXX_mipsel_unknown_linux_gnu=mipsel-linux-gnu-g++ \  
\  
AR_powerpc_unknown_linux_gnu=powerpc-linux-gnu-ar \  
CARGO_TARGET_POWERPC_UNKNOWN_LINUX_GNU_LINKER=powerpc-linux-gnu-gcc \  
CC_powerpc_unknown_linux_gnu=powerpc-linux-gnu-gcc \  
CXX_powerpc_unknown_linux_gnu=powerpc-linux-gnu-g++ \  
\  
AR_powerpc64_unknown_linux_gnu=powerpc64-linux-gnu-ar \  
CARGO_TARGET_POWERPC64_UNKNOWN_LINUX_GNU_LINKER=powerpc64-linux-gnu-gcc \  
CC_powerpc64_unknown_linux_gnu=powerpc64-linux-gnu-gcc \  
CXX_powerpc64_unknown_linux_gnu=powerpc64-linux-gnu-g++ \  
\  
AR_powerpc64le_unknown_linux_gnu=powerpc64le-linux-gnu-ar \  
CARGO_TARGET_POWERPC64LE_UNKNOWN_LINUX_GNU_LINKER=powerpc64le-linux-gnu-gcc \  
CC_powerpc64le_unknown_linux_gnu=powerpc64le-linux-gnu-gcc \  
CXX_powerpc64le_unknown_linux_gnu=powerpc64le-linux-gnu-g++ \  
\  
CARGO_TARGET_X86_64_UNKNOWN_LINUX_MUSL_LINKER=/musl/x86_64-unknown-linux-
musl/bin/musl-gcc \  
CC_x86_64_unknown_linux_musl=/musl/x86_64-unknown-linux-musl/bin/musl-gcc \  
CXX_x86_64_unknown_linux_musl=false  
  
ENTRYPOINT sh  

