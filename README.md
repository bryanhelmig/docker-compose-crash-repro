> This is fixed as of Docker for Mac Version 1.12.2-beta28 (12906).

## Docker for Mac Native Crashing on Heavy IO

To reproduce https://github.com/docker/hyperkit/issues/50 which seems predicated on heavy IO through osxfs - follow this:

```bash
git clone git@github.com:bryanhelmig/docker-compose-crash-repro.git
cd docker-compose-crash-repro
docker-compose build
docker-compose up -d
docker-compose logs -f -t web
```

Now visit `http://localhost:8888/` and do some **shift-click-refresh**ing - after a few times I fairly reliably get this:

```
web_1  | 2016-10-06T19:31:16.260066397Z [06/Oct/2016 19:31:16] "GET /static/js/0.js HTTP/1.1" 200 3005276
web_1  | 2016-10-06T19:31:16.305402868Z [06/Oct/2016 19:31:16] "GET /static/js/4.js HTTP/1.1" 200 3005276
web_1  | 2016-10-06T19:31:16.329396574Z [06/Oct/2016 19:31:16] "GET /static/js/1.js HTTP/1.1" 200 3005276
web_1  | 2016-10-06T19:31:16.340380030Z [06/Oct/2016 19:31:16] "GET /static/js/5.js HTTP/1.1" 200 3005276
web_1  | 2016-10-06T19:31:16.351149088Z [06/Oct/2016 19:31:16] "GET /static/js/3.js HTTP/1.1" 200 3005276
web_1  | 2016-10-06T19:31:16.422381149Z [06/Oct/2016 19:31:16] "GET /static/js/7.js HTTP/1.1" 200 3005276
web_1  | 2016-10-06T19:31:16.466906038Z [06/Oct/2016 19:31:16] "GET /static/js/6.js HTTP/1.1" 200 3005276
web_1  | 2016-10-06T19:31:16.629398654Z [06/Oct/2016 19:31:16] "GET /static/images/2.png HTTP/1.1" 200 1250
web_1  | 2016-10-06T19:31:16.660894374Z [06/Oct/2016 19:31:16] "GET /static/images/6.png HTTP/1.1" 200 1629
web_1  | 2016-10-06T19:31:16.663982442Z [06/Oct/2016 19:31:16] "GET /static/images/0.png HTTP/1.1" 200 1521
web_1  | 2016-10-06T19:31:16.687896989Z [06/Oct/2016 19:31:16] "GET /static/images/1.png HTTP/1.1" 200 1590
web_1  | 2016-10-06T19:31:16.688157570Z [06/Oct/2016 19:31:16] "GET /static/images/5.png HTTP/1.1" 200 2453
web_1  | 2016-10-06T19:31:16.689410612Z [06/Oct/2016 19:31:16] "GET /static/js/10.js HTTP/1.1" 200 3005276
web_1  | 2016-10-06T19:31:16.704951546Z [06/Oct/2016 19:31:16] "GET /static/js/11.js HTTP/1.1" 200 3005276
Unexpected API error for dockercomposecrashrepro_web_1 (HTTP code 500)
Response body:
dial unix /Users/bryanhelmig/Library/Containers/com.docker.docker/Data/*00000003.00000948: connect: connection refused
```

```
Oct  6 14:28:11 ip-172-27-239-114 Docker[24270] <Notice>: Negotiated transfuse notification channel for /Users
Oct  6 14:28:11 ip-172-27-239-114 Docker[24270] <Notice>: Negotiated transfuse notification channel for /Volumes
Oct  6 14:28:11 ip-172-27-239-114 Docker[24270] <Notice>: Negotiated transfuse notification channel for /tmp
Oct  6 14:28:11 ip-172-27-239-114 Docker[24270] <Notice>: Negotiated transfuse notification channel for /private
Oct  6 14:28:11 ip-172-27-239-114 Docker[24270] <Notice>: Negotiated transfuse notification channel for /host_docker_app
Oct  6 14:28:11 ip-172-27-239-114 Docker[24270] <Notice>: sending continue to client
Oct  6 14:28:11 ip-172-27-239-114 Docker[24271] <Notice>: Using protocol TwoThousand msize 8192
Oct  6 14:28:14 ip-172-27-239-114 Docker[24271] <Notice>: Creating resource Entry(tcp:0.0.0.0:8888:tcp:172.17.0.2:8888)
Oct  6 14:28:14 ip-172-27-239-114 Docker[24271] <Notice>: Write offset=0 data=[tcp:0.0.0.0:8888:tcp:172.17.0.2:8888] to file
Oct  6 14:28:14 ip-172-27-239-114 Docker[24271] <Notice>: attempting a best-effort bind of ::1:8888
Oct  6 14:28:14 ip-172-27-239-114 Docker[24271] <Notice>: Created instance tcp:0.0.0.0:8888:tcp:172.17.0.2:8888
Oct  6 14:28:15 ip-172-27-239-114 Docker[24272] <Notice>: Docker is responding
Oct  6 14:28:15 ip-172-27-239-114 Docker[599] <Notice>: VM started at 2016-10-06 12:28:15 -0700 PDT
Oct  6 14:28:15 ip-172-27-239-114 Docker[551] <Notice>: dockerState = Running
Oct  6 14:30:13 ip-172-27-239-114 Docker[24270] <Notice>: Creating resource Entry(9970e00f54f1df32f87dccd9fd788f16710c4dd472b1cf6e9844bfd5b6009577)
Oct  6 14:30:13 ip-172-27-239-114 Docker[24270] <Notice>: Write offset=0 data=[9970e00f54f1df32f87dccd9fd788f16710c4dd472b1cf6e9844bfd5b6009577:/Users/bryanhelmig/Code/docker-compose-crash-repro] to file
Oct  6 14:30:13 ip-172-27-239-114 Docker[24270] <Notice>: Volume.start 9970e00f54f1df32f87dccd9fd788f16710c4dd472b1cf6e9844bfd5b6009577 (paths = [/Users/bryanhelmig/Code/docker-compose-crash-repro])
Oct  6 14:30:13 ip-172-27-239-114 Docker[24270] <Notice>: Volume.start 9970e00f54f1df32f87dccd9fd788f16710c4dd472b1cf6e9844bfd5b6009577 (watches [/Users/bryanhelmig/Code/docker-compose-crash-repro -> /Users/bryanhelmig/Code/docker-compose-crash-repro])
Oct  6 14:30:13 ip-172-27-239-114 Docker[24270] <Notice>: Created instance 9970e00f54f1df32f87dccd9fd788f16710c4dd472b1cf6e9844bfd5b6009577
Oct  6 14:30:13 ip-172-27-239-114 Docker[24271] <Notice>: Creating resource Entry(tcp:0.0.0.0:8888:tcp:172.17.0.2:8888)
Oct  6 14:30:13 ip-172-27-239-114 Docker[24271] <Notice>: Write offset=0 data=[tcp:0.0.0.0:8888:tcp:172.17.0.2:8888] to file
Oct  6 14:30:13 ip-172-27-239-114 Docker[24271] <Notice>: attempting a best-effort bind of ::1:8888
Oct  6 14:30:13 ip-172-27-239-114 Docker[24271] <Notice>: Created instance tcp:0.0.0.0:8888:tcp:172.17.0.2:8888

##########################################################################################
###### it was running fine here - then i hard refreshed the page and it crashed.... ######
##########################################################################################

Oct  6 14:31:16 ip-172-27-239-114 Docker[24272] <Notice>: virtio-net-vpnkit: initialising, opts="uuid=9370d89c-e093-4eee-b9ca-6817aa703470,path=/Users/bryanhelmig/Library/Containers/com.docker.docker/Data/s50,macfile=/Users/bryanhelmig/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/mac.0"
Oct  6 14:31:16 ip-172-27-239-114 Docker[24272] <Notice>: Assertion failed: (!REPLY_RING_EMPTY(sc)), function send_response_common, file src/pci_virtio_sock.c, line 917.
Oct  6 14:31:16 ip-172-27-239-114 Docker[24272] <Notice>: Interface will have uuid 9370d89c-e093-4eee-b9ca-6817aa703470
Oct  6 14:31:16 ip-172-27-239-114 Docker[24272] <Notice>: Connection established with MAC=c0:ff:ee:c0:ff:ee and MTU 1500
Oct  6 14:31:16 ip-172-27-239-114 Docker[24272] <Notice>: virtio-9p: initialising path=/Users/bryanhelmig/Library/Containers/com.docker.docker/Data/s40,tag=db
Oct  6 14:31:16 ip-172-27-239-114 Docker[24272] <Notice>: virtio-9p: initialising path=/Users/bryanhelmig/Library/Containers/com.docker.docker/Data/s51,tag=port
Oct  6 14:31:16 ip-172-27-239-114 Docker[24272] <Notice>: linkname /Users/bryanhelmig/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/tty
Oct  6 14:31:16 ip-172-27-239-114 Docker[24272] <Notice>: COM1 connected to /dev/ttys000
Oct  6 14:31:16 ip-172-27-239-114 Docker[24272] <Notice>: COM1 linked to /Users/bryanhelmig/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/tty
Oct  6 14:31:16 ip-172-27-239-114 Docker[24270] <Error>: Fatal unexpected exception: Socket.Closed
Oct  6 14:31:16 ip-172-27-239-114 Docker[24271] <Notice>: PPP.listen: closing connection
Oct  6 14:31:16 ip-172-27-239-114 Docker[24271] <Error>: Socket.Stream: caught Uwt.Uwt_error(Uwt.ENOTCONN, "shutdown", "")
Oct  6 14:31:16 ip-172-27-239-114 Docker[588] <Notice>: Reap com.docker.osxfs (pid 24270): exit status 1
Oct  6 14:31:16 ip-172-27-239-114 Docker[24271] <Error>: Socket.Stream: caught Uwt.Uwt_error(Uwt.ENOTCONN, "shutdown", "")
Oct  6 14:31:16 ip-172-27-239-114 Docker[24271] <Error>: Socket.Stream: caught Uwt.Uwt_error(Uwt.ECONNREFUSED, "pipe_connect", "")
--- last message repeated 1 time ---
Oct  6 14:31:16 ip-172-27-239-114 Docker[599] <Notice>: VM shutdown at 2016-10-06 12:31:16 -0700 PDT
Oct  6 14:31:16 ip-172-27-239-114 Docker[588] <Notice>: Reap com.docker.driver.amd64-linux (pid 24272): exit status 0
Oct  6 14:31:16 ip-172-27-239-114 Docker[24271] <Error>: Socket.Stream: caught Uwt.Uwt_error(Uwt.ECONNREFUSED, "pipe_connect", "")
--- last message repeated 1 time ---
Oct  6 14:31:16 ip-172-27-239-114 Docker[551] <Notice>: dockerState = Starting
Oct  6 14:31:16 ip-172-27-239-114 Docker[24271] <Error>: Socket.Stream: caught Uwt.Uwt_error(Uwt.ECONNREFUSED, "pipe_connect", "")
--- last message repeated 19 times ---
Oct  6 14:31:16 ip-172-27-239-114 Docker[24271] <Error>: Socket.Stream: caught Uwt.Uwt_error(Uwt.ENOTCONN, "shutdown", "")
Oct  6 14:31:16 ip-172-27-239-114 Docker[24271] <Error>: Socket.Stream: caught Uwt.Uwt_error(Uwt.ECONNREFUSED, "pipe_connect", "")
--- last message repeated 2 times ---
Oct  6 14:31:16 ip-172-27-239-114 Docker[24271] <Error>: Socket.Stream: caught Uwt.Uwt_error(Uwt.ENOTCONN, "shutdown", "")
--- last message repeated 1 time ---
Oct  6 14:31:16 ip-172-27-239-114 Docker[24271] <Error>: Socket.Stream: caught Uwt.Uwt_error(Uwt.ECONNREFUSED, "pipe_connect", "")
--- last message repeated 2 times ---
Oct  6 14:31:16 ip-172-27-239-114 Docker[24271] <Error>: Socket.Stream: caught Uwt.Uwt_error(Uwt.ENOTCONN, "shutdown", "")
Oct  6 14:31:16 ip-172-27-239-114 Docker[24271] <Error>: Socket.Stream: caught Uwt.Uwt_error(Uwt.ECONNREFUSED, "pipe_connect", "")
--- last message repeated 347 times ---
Oct  6 14:31:17 ip-172-27-239-114 Docker[588] <Notice>: Stop 1 children with order 1: com.docker.driver.amd64-linux (pid 24272)
Oct  6 14:31:17 ip-172-27-239-114 Docker[588] <Notice>: Stop 2 children with order 2: com.docker.osxfs (pid 24270), com.docker.slirp (pid 24271)
Oct  6 14:31:17 ip-172-27-239-114 Docker[588] <Notice>: Signal terminated to com.docker.slirp (pid 24271)
Oct  6 14:31:17 ip-172-27-239-114 Docker[588] <Notice>: Reap com.docker.slirp (pid 24271): signal: terminated
Oct  6 14:31:17 ip-172-27-239-114 Docker[588] <Notice>: Starting com.docker.osxfs, com.docker.slirp, com.docker.driver.amd64-linux
Oct  6 14:31:17 ip-172-27-239-114 Docker[588] <Notice>: Start com.docker.osxfs (pid 25080)
Oct  6 14:31:17 ip-172-27-239-114 Docker[588] <Notice>: Start com.docker.slirp (pid 25081)
Oct  6 14:31:17 ip-172-27-239-114 Docker[588] <Notice>: Start com.docker.driver.amd64-linux (pid 25082)
Oct  6 14:31:17 ip-172-27-239-114 Docker[25080] <Notice>: Logging to Apple System Log
Oct  6 14:31:17 ip-172-27-239-114 Docker[25081] <Notice>: Logging to Apple System Log
Oct  6 14:31:17 ip-172-27-239-114 Docker[25081] <Notice>: Setting handler to ignore all SIGPIPE signals
Oct  6 14:31:17 ip-172-27-239-114 Docker[25081] <Notice>: vpnkit version 9cb6374ebfd0656961901478e9fc8cf65d000678 with hostnet version local  uwt version 0.0.3 hvsock version 0.10.0
Oct  6 14:31:17 ip-172-27-239-114 Docker[25081] <Notice>: starting port_forwarding port_control_url:fd:4 vsock_path:/Users/bryanhelmig/Library/Containers/com.docker.docker/Data/@connect
Oct  6 14:31:17 ip-172-27-239-114 Docker[25081] <Notice>: hosts file has bindings for localhost broadcasthost localhost localhost zapier.local zapier.dev zapier.part activate.adobe.com practivate.adobe.com ereg.adobe.com activate.wip3.adobe.com wip3.adobe.com 3dns-3.adobe.com 3dns-2.adobe.com adobe-dns.adobe.com adobe-dns-2.adobe.com adobe-dns-3.adobe.com ereg.wip3.adobe.com activate-sea.adobe.com wwis-dubc1-vip60.adobe.com activate-sjc0.adobe.com hl2rcv.adobe.com activate.adobe.com practivate.adobe.com ereg.adobe.com activate.wip3.adobe.com wip3.adobe.com p.jbugk.com 3dns-3.adobe.com 3dns-2.adobe.com adobe-dns.adobe.com adobe-dns-2.adobe.com adobe-dns-3.adobe.com ereg.wip3.adobe.com activate-sea.adobe.com wwis-dubc1-vip60.adobe.com activate-sjc0.adobe.com hl2rcv.adobe.com 192.150.14.69 192.150.18.101 192.150.18.108 192.150.22.40 192.150.8.100 192.150.8.118 209-34-83-73.ood.opsource.net 3dns-1.adobe.com 3dns-2.adobe.com 3dns-2.adobe.com 3dns-3.adobe.com 3dns-3.adobe.com 3dns-4.adobe.com 3dns.adobe.com activate-sea.adobe.com activate-sea.adobe.com activate-sjc0.adobe.com activate-sjc0.adobe.com activate.adobe.com activate.adobe.com activate.wip.adobe.com activate.wip1.adobe.com activate.wip2.adobe.com activate.wip3.adobe.com activate.wip3.adobe.com activate.wip4.adobe.com adobe-dns-1.adobe.com adobe-dns-2.adobe.com adobe-dns-2.adobe.com adobe-dns-3.adobe.com adobe-dns-3.adobe.com adobe-dns-4.adobe.com adobe-dns.adobe.com adobe-dns.adobe.com adobe.activate.com adobeereg.com crl.verisign.net CRL.VERISIGN.NET.* ereg.adobe.com ereg.adobe.com ereg.wip.adobe.com ereg.wip1.adobe.com ereg.wip2.adobe.com ereg.wip3.adobe.com ereg.wip3.adobe.com ereg.wip4.adobe.com hl2rcv.adobe.com ood.opsource.net practivate.adobe practivate.adobe.* practivate.adobe.com practivate.adobe.com practivate.adobe.ipp practivate.adobe.newoa practivate.adobe.ntp tss-geotrust-crl.thawte.com wip.adobe.com wip1.adobe.com wip2.adobe.com wip3.adobe.com wip3.adobe.com wip4.adobe.com wwis-dubc1-vip60.adobe.com wwis-dubc1-vip60.adobe.com wwis-dubc1-vip60.adobe.com dockerhost dockerhost.zapier.com zapier-tunnel.local abc.zapier-tunnel.local def.zapier-tunnel.local ghi.zapier-tunnel.local jkl.zapier-tunnel.local
Oct  6 14:31:17 ip-172-27-239-114 Docker[25082] <Notice>: Acquired hypervisor lock
Oct  6 14:31:17 ip-172-27-239-114 Docker[25082] <Notice>: Docker is not responding: Get http://./info: dial unix /Users/bryanhelmig/Library/Containers/com.docker.docker/Data/*00000003.00000948: connect: connection refused: waiting 0.5s
Oct  6 14:31:17 ip-172-27-239-114 Docker[25082] <Notice>: OSX version = 10.11.6, default value of on-sleep = freeze
Oct  6 14:31:18 ip-172-27-239-114 Docker[25082] <Notice>: hypervisor: native
Oct  6 14:31:18 ip-172-27-239-114 Docker[25082] <Notice>: filesystem: osxfs
Oct  6 14:31:18 ip-172-27-239-114 Docker[25082] <Notice>: network: hybrid
Oct  6 14:31:18 ip-172-27-239-114 Docker[25080] <Notice>: Using protocol TwoThousand msize 16384
Oct  6 14:31:18 ip-172-27-239-114 Docker[25082] <Notice>: Hypervisor: native; BootProtocol: direct; UefiBootDisk: /Users/bryanhelmig/UefiBoot.qcow2
Oct  6 14:31:18 ip-172-27-239-114 Docker[25082] <Notice>: Syslog socket is /Users/bryanhelmig/Library/Containers/com.docker.docker/Data/*00000002.00000202
Oct  6 14:31:18 ip-172-27-239-114 Docker[25082] <Notice>: Logfile is /Users/bryanhelmig/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/syslog
Oct  6 14:31:18 ip-172-27-239-114 Docker[25082] <Notice>: Launched[25086]: /Applications/Docker.app/Contents/MacOS/com.docker.hyperkit -A -m 6G -c 4 -u -s 0:0,hostbridge -s 31,lpc -s 2:0,virtio-vpnkit,uuid=9370d89c-e093-4eee-b9ca-6817aa703470,path=/Users/bryanhelmig/Library/Containers/com.docker.docker/Data/s50,macfile=/Users/bryanhelmig/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/mac.0 -s 3,virtio-blk,file:///Users/bryanhelmig/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/Docker.qcow2?sync=1&buffered=1,format=qcow -s 4,virtio-9p,path=/Users/bryanhelmig/Library/Containers/com.docker.docker/Data/s40,tag=db -s 5,virtio-rnd -s 6,virtio-9p,path=/Users/bryanhelmig/Library/Containers/com.docker.docker/Data/s51,tag=port -s 7,virtio-sock,guest_cid=3,path=/Users/bryanhelmig/Library/Containers/com.docker.docker/Data,guest_forwards=2376;1525 -l com1,autopty=/Users/bryanhelmig/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/tty,log=/Users/bryanhelmig/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/console-ring -f kexec,/Applications/Docker.app/Contents/Resources/moby/vmlinuz64,/Applications/Docker.app/Contents/Resources/moby/initrd.img,earlyprintk=serial console=ttyS0 com.docker.driver="com.docker.driver.amd64-linux", com.docker.database="com.docker.driver.amd64-linux" ntp=gateway mobyplatform=mac -F /Users/bryanhelmig/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/hypervisor.pid
Oct  6 14:31:18 ip-172-27-239-114 Docker[25082] <Notice>: SC database lists DNS servers: 10.0.0.2
Oct  6 14:31:18 ip-172-27-239-114 Docker[25082] <Notice>: SC database lists search domains: utun0.viscosity
Oct  6 14:31:18 ip-172-27-239-114 Docker[25081] <Notice>: attempting to reconnect to database
Oct  6 14:31:18 ip-172-27-239-114 Docker[25081] <Notice>: reconnected transport layer
Oct  6 14:31:18 ip-172-27-239-114 Docker[25081] <Notice>: remove connection limit
Oct  6 14:31:18 ip-172-27-239-114 Docker[25081] <Notice>: updating search domains to utun0.viscosity
Oct  6 14:31:18 ip-172-27-239-114 Docker[25081] <Notice>: updating resolvers to nameserver 10.0.0.2#53
Oct  6 14:31:18 ip-172-27-239-114 Docker[25081] <Notice>: using DNS forwarders on 10.0.0.2#53
Oct  6 14:31:18 ip-172-27-239-114 Docker[25081] <Notice>: allowing binds to any IP addresses
Oct  6 14:31:18 ip-172-27-239-114 Docker[25081] <Notice>: Creating slirp server pcap_settings:disabled peer_ip:192.168.65.2 local_ip:192.168.65.1 domain_search:utun0.viscosity
Oct  6 14:31:18 ip-172-27-239-114 Docker[25081] <Notice>: PPP.negotiate: received ((magic VMN3T)(version 1)(commit 179c18cae7079a6e6994bf2474b337dca2762d5b))
Oct  6 14:31:18 ip-172-27-239-114 Docker[25081] <Notice>: PPP.negotiate: received (Ethernet 9370d89c-e093-4eee-b9ca-6817aa703470)
Oct  6 14:31:18 ip-172-27-239-114 Docker[25082] <Notice>: virtio-net-vpnkit: magic=VMN3T version=1 commit=0123456789012345678901234567890123456789
Oct  6 14:31:18 ip-172-27-239-114 Docker[25081] <Notice>: PPP.negotiate: sending ((mtu 1500)(max_packet_size 1550)(client_macaddr c0:ff:ee:c0:ff:ee))
Oct  6 14:31:18 ip-172-27-239-114 Docker[25081] <Notice>: PPP.listen: called a second time: doing nothing
Oct  6 14:31:18 ip-172-27-239-114 Docker[25081] <Notice>: TCP/IP ready
Oct  6 14:31:18 ip-172-27-239-114 Docker[25081] <Notice>: stack connected
Oct  6 14:31:18 ip-172-27-239-114 Docker[25082] <Notice>: mirage_block_open: file:///Users/bryanhelmig/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/Docker.qcow2?sync=1&buffered=1
Oct  6 14:31:18 ip-172-27-239-114 Docker[25082] <Notice>: mirage_block_open: file:///Users/bryanhelmig/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/Docker.qcow2?sync=1&buffered=1 returning 0
Oct  6 14:31:18 ip-172-27-239-114 Docker[25082] <Notice>: mirage_block_stat
Oct  6 14:31:18 ip-172-27-239-114 Docker[25082] <Notice>: vsock init 7:0 = /Users/bryanhelmig/Library/Containers/com.docker.docker/Data, guest_cid = 00000003
Oct  6 14:31:20 ip-172-27-239-114 Docker[25082] <Notice>:
    rdmsr to register 0x34 on vcpu 2
Oct  6 14:31:21 ip-172-27-239-114 Docker[25082] <Notice>: Docker is not responding: Get http://./info: EOF: waiting 0.5s
--- last message repeated 4 times ---
```

### Rebuilding Assets w/ More/Less Content

Default builds a dozen large JS files (3mb each), and 600 128px pngs, but you can tweak that to apply more/less pressure on IO:

```bash
vim make_files.py # change JS_COUNT, JS_BYTES_EACH, IMAGE_COUNT, IMAGE_PX_SIZE constants
rm -rf assets
docker-compose run web python make_files.py
# re-run docker-compose up -d, etc...
```
