sudo killall openvpn
modprobe tun
sudo openvpn --config /etc/openvpn/client.conf 