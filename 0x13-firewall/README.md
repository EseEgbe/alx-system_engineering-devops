# Project Firewall
Project done during **Software Engineering program** at **ALX**.
Its aim was to learn how to used `ufw` to configure firewalls on issued web servers.

## Technologies
* Scripts are written in Bash 5.2.15
* Tested on Ubuntu 20.04 LTS

## Files

| Filename | Description |
| -------- | ----------- |
| `-block_all_incoming_traffic_but` | Bash script that installs a `ufw` firewall to block all incoming traffic except for ports `22`, `443` and `80` on a web server. |
| `100-port_forwarding` | `ufw` configuration file that configures a firewall to redirect port `8080/TCP` to port `80/TCP`. |
